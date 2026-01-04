import os
import re
import pickle

try:
    import polars as pl
except ImportError:
    pl = None
try:
    import pandas as pd
except ImportError:
    pd = None

pkg_dir, pkg_filename = os.path.split(__file__)

def load_dict(data_path: str = os.path.join(pkg_dir, 'data', 'codelist.pickle')):
    """
    Load a pickle file containing the countrycode translations.
    
    Parameters:
    data_path (str):
        The path to a `.pickle` file to be used for matching codes.

    """

    fileextension = os.path.splitext(data_path)[1]

    if fileextension != '.pickle':
        raise NotImplementedError(f'Custom dicts with `{fileextension}` are not implemented yet. Please use a `.pickle` file or None (to use the default).')

    try:
        with open(data_path, 'rb') as f:
            codelist = pickle.load(f)
    
    except:
        raise FileNotFoundError(f'Could not find file at `{data_path}`. Please make sure the file exists at the provided path.')
    
    return codelist


def countrycode(
    sourcevar=["DZA", "CAN"], origin="iso3c", destination="country.name.en", custom_dict = None 
):
    """
    Convert country codes or names from one format to another.

    This function takes a list, string, or Polars Series of country codes or names, and converts them to the desired
    format, such as ISO 3-letter codes, country names in different languages, etc.

    Parameters:
    sourcevar (list, str, int, or polars.series.series.Series, optional):
        A list, string, integer, or Polars Series of country codes or names to be converted. Default is ['DZA', 'CAN'].
    origin (str, optional):
        The format of the input country codes or names. Default is 'iso3c'.
    destination (str, optional):
        The desired format of the output country codes or names. Default is 'country.name.en'.
    custom_dict (str, dict, optional):
        A custom dictionary to be used. Can either be a path to an existing `.pickle` file or a dictionary. Default is None, i.e. the default dict is used. 

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
    NotImplementedError:
        If the custom_file is a string (path to dict file) but not a `.pickle` file.
        If the custom_dict argument is neither str, None or dict.
    FileNotFoundError:
        If the custom_file is a string (path to dict file) and a pickle file but does not exist. 

    Example:
    >>> countrycode(['DZA', 'CAN'], origin='iso3c', destination='country.name.en')
    ['Algeria', 'Canada']

    Note:
    This function uses two helper functions (`replace_regex` and `replace_exact`) to perform the actual conversion.
    """

    # Load the codelist dict.
    if isinstance(custom_dict, str):
        # If the custom dict argument is a string it will be interpreted as a path to load 
        # the custom dict from.
        codelist = load_dict(custom_dict)
    
    elif isinstance(custom_dict, dict):
        codelist = custom_dict

    elif custom_dict == None:
        # Default data path is just data/codelist.pickle
        codelist = load_dict()

    else:
        raise NotImplementedError(f'The custom_dict has to be either None (to use the default dict), dict or str NOT {type(custom_dict)}')


    # user convenience shortcuts only for default dict
    if origin == "country.name":
        origin = "country.name.en.regex"

    if origin in [
        "country.name.en",
        "country.name.fr",
        "country.name.de", 
        "country.name.it",
    ]:
        origin = origin + ".regex"

    if destination == "country.name":
        destination = "country.name.en"

    if destination not in codelist.keys():
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

    sourcevar_series = sourcevar
    if pl:
        if isinstance(sourcevar, pl.series.series.Series):
            sourcevar_series = sourcevar.to_list()
    if pd:
        if isinstance(sourcevar, pd.Series):
            sourcevar_series = sourcevar.to_list()
    if isinstance(sourcevar, (str, int)):
        sourcevar_series = [sourcevar]

    # conversion
    if origin in [
        "country.name.en.regex",
        "country.name.fr.regex",
        "country.name.de.regex",
        "country.name.it.regex",
    ]:
        out = replace_regex(sourcevar_series, origin, destination, codelist)
    else:
        out = replace_exact(sourcevar_series, origin, destination, codelist)

    # output type
    if isinstance(sourcevar, (str, int)):
        return out[0]
    elif pl and isinstance(sourcevar, pl.series.series.Series):
        return pl.Series(out)
    elif pd and isinstance(sourcevar, pd.Series):
        return pd.Series(out)
    else:
        return out


def get_first_match(pattern, string_list):
    for string in string_list:
        match = pattern.search(string)
        if match:
            return match.group()
    return None


def replace_exact(sourcevar, origin, destination, codelist):
    out = []
    for string in sourcevar:
        match_found = False
        for position, origin_i in enumerate(codelist[origin]):
            if origin_i is None or codelist[destination][position] is None:
                continue
            if string == origin_i:
                if (
                    isinstance(codelist[destination][position], str)
                    and codelist[destination][position].isdigit()
                ):
                    out.append(int(codelist[destination][position]))
                else:
                    out.append(codelist[destination][position])
                match_found = True
                break
        if not match_found:
            out.append(None)
    return out


def replace_regex(sourcevar, origin, destination, codelist):
    sourcevar_unique = list(set(sourcevar))
    o = []
    d = []
    for i, (val_origin, val_destination) in enumerate(
        zip(codelist[origin], codelist[destination])
    ):
        if val_origin is not None and val_destination is not None:
            o.append(re.compile(val_origin, flags=re.IGNORECASE))
            d.append(val_destination)

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
    out = [
        int(mapping[i])
        if mapping[i] and isinstance(mapping[i], str) and mapping[i].isdigit()
        else mapping[i]
        for i in sourcevar
    ]
    return out
