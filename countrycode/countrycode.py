# TODO: sanitize input
# white space only if string
# sourcevar = [str(x).strip() for x in sourcevar]
# round numeric if
# sourcevar = [f"{x:.0f}" for x in sourcevar]

import re
import os
import polars as pl
from copy import copy

pkg_dir, pkg_filename = os.path.split(__file__)
data_path = os.path.join(pkg_dir, "data", "codelist.csv")
codelist = pl.read_csv(data_path)

def countrycode(sourcevar=['DZA', 'CAN'], origin='iso3c', destination='country.name.en'):
    # user convenience shortcuts
    if origin == "country.name":
        origin = "country.name.en.regex"

    if origin in ['country.name.en', 'country.name.fr', 'country.name.de', 'country.name.it']:
        origin = origin + ".regex"

    if destination == "country.name":
        destination = "country.name.en"

    # sanity checks
    if origin not in codelist.columns:
        raise ValueError(f"origin {origin} not found in the code list.")

    if destination not in codelist.columns:
        raise ValueError(f"destination {destination} not found in the code list.")

    valid = ["cctld", "country.name", "country.name.de", "country.name.fr", "country.name.it", "cowc", "cown", "dhs", "ecb", "eurostat", "fao", "fips", "gaul", "genc2c", "genc3c", "genc3n", "gwc", "gwn", "imf", "ioc", "iso2c", "iso3c", "iso3n", "p5c", "p5n", "p4c", "p4n", "un", "un_m49", "unicode.symbol", "unhcr", "unpd", "vdem", "wb", "wb_api2c", "wb_api3c", "wvs", "country.name.en.regex", "country.name.de.regex", "country.name.fr.regex", "country.name.it.regex"]
    if origin not in valid:
        raise ValueError("origin must be one of: " + ", ".join(valid))

    # we want to operate on polars Series, but allow and return single values
    if isinstance(sourcevar, str) | isinstance(sourcevar, int):
        sourcevar_series = pl.Series([sourcevar])
    elif isinstance(sourcevar, list):
        sourcevar_series = pl.Series(sourcevar)
    elif isinstance(sourcevar, pl.series.series.Series):
        sourcevar_series = sourcevar
    else:
        raise ValueError(f"sourcevar must be a string, list, or polars series. Got {type(sourcevar)}")

    # conversion
    if origin in ['country.name.en.regex', 'country.name.fr.regex', 'country.name.de.regex', 'country.name.it.regex']:
        out = replace_regex(sourcevar_series, origin, destination)
    else:
        out = replace_exact(sourcevar_series, origin, destination)

    # output type
    if isinstance(sourcevar, str) | isinstance(sourcevar, int):
        return out[0]
    elif isinstance(sourcevar, list) & isinstance(out, pl.series.series.Series):
        return out.to_list()
    elif isinstance(out, list) & isinstance(sourcevar, pl.series.series.Series):
        return pl.Series(out)
    else:
        return out


def get_first_match(pattern, string_list):
    for string in string_list:
        match = pattern.search(string)
        if match:
            return match.group()
    return None


def replace_exact(sourcevar, origin, destination):
    codelist_nonull = codelist[[origin, destination]].drop_nulls()
    mapping = dict(zip(codelist_nonull[origin], codelist_nonull[destination]))
    out = sourcevar.map_dict(mapping)
    return out


def replace_regex(sourcevar, origin, destination):
    sourcevar_unique = sourcevar.unique()
    codelist_nonull = codelist[[origin, destination]].drop_nulls()
    o = [re.compile(x, flags = re.IGNORECASE) for x in codelist_nonull[origin]]
    d = codelist_nonull[destination]
    result = []
    for string in sourcevar_unique:
        match_found = False
        for position, regex in enumerate(o):
            if re.match(regex, string):
                result.append(d[position])
                match_found = True
                break
        if not match_found:
            result.append(None)
    mapping = dict(zip(sourcevar_unique, result))
    out = sourcevar.map_dict(mapping)
    return out