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
data = pl.read_csv(data_path)

def countrycode(sourcevar=['DZA', 'CAN'], origin='iso3c', destination='country.name.en'):
    # user convenience shortcut
    if origin == "country.name":
        origin = "country.name.en.regex"

    # sanity checks
    if origin not in data.columns:
        raise ValueError(f"origin {origin} not found in the code list.")

    if destination not in data.columns:
        raise ValueError(f"destination {destination} not found in the code list.")

    # we want to operate on polars Series, but allow and return single values
    if isinstance(sourcevar, str) | isinstance(sourcevar, int):
        sourcevar_series = pl.Series([sourcevar])
    elif isinstance(sourcevar, list):
        sourcevar_series = pl.Series(sourcevar)
    elif isinstance(sourcevar, pl.series.series.Series):
        sourcevar_series = sourcevar
    else:
        raise ValueError(f"sourcevar must be a string, list, or polars series. Got {type(sourcevar)}")

    # convesion
    if origin in ['country.name.en.regex', 'country.name.fr.regex', 'country.name.de.regex', 'country.name.it.regex']:
        out = replace_regex(sourcevar_series, origin, destination)
    else:
        out = replace_exact(sourcevar_series, origin, destination)

    # output type
    if isinstance(sourcevar, str) | isinstance(sourcevar, int):
        return out[0]
    elif isinstance(sourcevar, list) & isinstance(out, pl.series.series.Series):
        return out.to_list()
    else:
        return out


def get_first_match(pattern, string_list):
    for string in string_list:
        match = pattern.search(string)
        if match:
            return match.group()
    return None


def replace_exact(sourcevar, origin, destination):
    mapping = dict(zip(data[origin], data[destination]))
    out = sourcevar.map_dict(mapping)
    return out


def replace_regex(sourcevar, origin, destination):
    result = []
    mapping = dict(zip(data[origin], data[destination]))
    for string in sourcevar:
        match_found = False
        for regex in mapping.keys():
            if re.match(regex, string, flags = re.IGNORECASE):
                result.append(mapping[regex])
                match_found = True
                break
        if not match_found:
            result.append(None)
    return result