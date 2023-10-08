import os
import re


class GenericDataframe:
    def __init__(self, package, data):
        self.package = package
        self.data = data
        if package == "polars" or package == "pandas":
            self.columns = self.data.columns
        else:
            self.columns = self.data.keys()

    def get_nonull(self, origin, destination):
        if self.package == "polars":
            return self.data[[origin, destination]].drop_nulls()
        elif self.package == "pandas":
            return self.data[[origin, destination]].dropna()
        else:
            nonull = {origin: [], destination:[]}
            for i in range(len(self.data[origin])):
                if self.data[origin][i] != '' and self.data[destination][i] != '':
                    nonull[origin].append(self.data[origin][i])
                    nonull[destination].append(self.data[destination][i])
            return nonull

class GenericSeries:
    def __init__(self, package, sourcevar):
        if isinstance(sourcevar, str) | isinstance(sourcevar, int):
            sourcevar = [sourcevar]
        self.package = package
        if package == "polars":
            self.series = pl.Series(sourcevar)
        elif package == "pandas":
            self.series = pd.Series(sourcevar)
        else:
            self.series = sourcevar           

    def unique(self):
        if self.package == "polars" or self.package == "pandas":
            return self.series.unique()
        else:
            return list(set(self.series))

    def map_dict(self, remapping):
        if self.package == "polars":
            return self.series.map_dict(remapping)
        elif self.package == "pandas":
            return self.series.map(remapping)
        else:
            return [remapping[i] for i in self.series]

    def out_to_list(self, out):
        if self.package == "polars":
            return out.to_list()
        elif self.package == "pandas":
            return out.tolist()
        else:
            return out 


pkg_dir, pkg_filename = os.path.split(__file__)
data_path = os.path.join(pkg_dir, "data", "codelist.csv")

try:
    import polars as pl
except ImportError:
    pl = None
try:
    import pandas as pd
except ImportError:
    pd = None

if pl:
    data = pl.read_csv(data_path)
    codelist = GenericDataframe("polars", data)
elif pd:
    data = pd.read_csv(data_path)
    codelist = GenericDataframe("pandas", data)
else:
    import csv
    with open(data_path) as f:
        rows = [row.strip().split(",") for row in f]
    data = {row[0]: list(row[1:]) for row in zip(*rows)}
    codelist = GenericDataframe(None, data)


def countrycode(sourcevar=["DZA", "CAN"], origin="iso3c", destination="country.name.en"):
    """
    Convert country codes or names from one format to another.

    This function takes a list, string, or Polars Series of country codes or names, and converts them to the desired
    format, such as ISO 3-letter codes, country names in different languages, etc.

    Parameters:
    sourcevar (list, str, or polars.series.series.Series, optional):
        A list, string, or Polars Series of country codes or names to be converted. Default is ['DZA', 'CAN'].
    origin (str, optional):
        The format of the input country codes or names. Default is 'iso3c'.
    destination (str, optional):
        The desired format of the output country codes or names. Default is 'country.name.en'.

    Returns:
    list, str, or polars.series.series.Series:
        The converted country codes or names in the desired format. The output type depends on the input type:
        - If `sourcevar` is a string or int, returns a string.
        - If `sourcevar` is a list, returns a list.
        - If `sourcevar` is a Polars Series, returns a Polars Series.

    Raises:
    ValueError:
        If the `origin` or `destination` format is not one of the supported formats.
        If the input `sourcevar` is not a string, list, or Polars Series.

    Example:
    >>> countrycode(['DZA', 'CAN'], origin='iso3c', destination='country.name.en')
    ['Algeria', 'Canada']

    Note:
    This function uses two helper functions (`replace_regex` and `replace_exact`) to perform the actual conversion.
    """

    # user convenience shortcuts
    if origin == "country.name":
        origin = "country.name.en.regex"

    if origin in ["country.name.en", "country.name.fr", "country.name.de", "country.name.it"]:
        origin = origin + ".regex"

    if destination == "country.name":
        destination = "country.name.en"

    if destination not in codelist.columns:
        raise ValueError("destination must be one of: " + "".join(codelist.columns))

    valid = [
        "cctld",
        "country.name",
        "country.name.de",
        "country.name.fr",
        "country.name.it",
        "cowc",
        "cown",
        "dhs",
        "ecb",
        "eurostat",
        "fao",
        "fips",
        "gaul",
        "genc2c",
        "genc3c",
        "genc3n",
        "gwc",
        "gwn",
        "imf",
        "ioc",
        "iso2c",
        "iso3c",
        "iso3n",
        "p5c",
        "p5n",
        "p4c",
        "p4n",
        "un",
        "un_m49",
        "unicode.symbol",
        "unhcr",
        "unpd",
        "vdem",
        "wb",
        "wb_api2c",
        "wb_api3c",
        "wvs",
        "country.name.en.regex",
        "country.name.de.regex",
        "country.name.fr.regex",
        "country.name.it.regex",
    ]
    if origin not in valid:
        raise ValueError("origin must be one of: " + ", ".join(valid))


    # The only case the package used by sourcevar is not the same as the package used by codelist
    # is when codelist is in polars and sourcevar is in pandas.
    if codelist.package == "polars":
        if pd and isinstance(sourcevar, pd.Series):
            sourcevar_series = GenericSeries("pandas", sourcevar)
        else:
            sourcevar_series = GenericSeries("polars", sourcevar)
    else:
        sourcevar_series = GenericSeries(codelist.package, sourcevar)


    # conversion
    if origin in [
        "country.name.en.regex",
        "country.name.fr.regex",
        "country.name.de.regex",
        "country.name.it.regex",
    ]:
        out = replace_regex(sourcevar_series, origin, destination)
    else:
        out = replace_exact(sourcevar_series, origin, destination)


    if isinstance(sourcevar, str) | isinstance(sourcevar, int):
        return out[0]
    elif isinstance(sourcevar, list):
        return sourcevar_series.out_to_list(out)
    else:
        return out


def get_first_match(pattern, string_list):
    for string in string_list:
        match = pattern.search(string)
        if match:
            return match.group()
    return None


def replace_exact(sourcevar, origin, destination):
    codelist_nonull = codelist.get_nonull(origin, destination)
    mapping = dict(zip(codelist_nonull[origin], codelist_nonull[destination]))
    out = sourcevar.map_dict(mapping)
    return out


def replace_regex(sourcevar, origin, destination):
    sourcevar_unique = sourcevar.unique()
    codelist_nonull = codelist.get_nonull(origin, destination)
    o = [re.compile(x, flags=re.IGNORECASE) for x in codelist_nonull[origin]]  # noqa: E251
    d = codelist_nonull[destination]  # noqa: E251
    result = []
    for string in sourcevar_unique:
        match_found = False
        for position, regex in enumerate(o):
            if re.search(regex, string):
                result.append(d[position])
                match_found = True
                break
        if not match_found:
            result.append(None)
    mapping = dict(zip(sourcevar_unique, result))
    out = sourcevar.map_dict(mapping)
    return out