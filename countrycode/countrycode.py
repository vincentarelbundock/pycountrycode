import re
import os
import csv
from copy import copy

pkg_dir, pkg_filename = os.path.split(__file__)
data_path = os.path.join(pkg_dir, "data", "codelist.csv")
with open(data_path, 'r') as f:
    reader = csv.reader(f)
    data = zip(*reader)
    data = [(x[0], x[1:]) for x in data]
    data = dict(data)

def countrycode(sourcevar=['DZA', 'CAN'], origin='iso3c', destination='country.name.en'):

    # sanity checks
    if not isinstance(origin, str):
        raise TypeError(f"Expected a string, got {type(argument).__name__}")
    else:
        if origin in ['country.name.en.regex', 'country.name.fr.regex', 'country.name.de.regex', 'country.name.it.regex']:
            origin_regex = True
        else:
            origin_regex = False
    if not isinstance(destination, str):
        raise TypeError(f"Expected a string, got {type(destination).__name__}")
    if origin not in data.keys():
        raise ValueError(f"origin {origin} not found in the code list.")
    else:
        origin = data[origin]
    if destination not in data.keys():
        raise ValueError(f"destination {destination} not found in the code list.")
    else:
        destination = data[destination]


    # we want to operate on lists, but allow and return single values
    loner = False
    if isinstance(sourcevar, str):
        sourcevar = [sourcevar]
        loner = True


    if origin_regex:
        out = replace_regex(sourcevar, origin, destination)
    else:
        out = replace_exact(sourcevar, origin, destination)

    # TODO: sanitize input
    # white space only if string
    # sourcevar = [str(x).strip() for x in sourcevar]
    # round numeric if
    # sourcevar = [f"{x:.0f}" for x in sourcevar]

    if loner:
        out = out[0]

    return out


def get_first_match(pattern, string_list):
    for string in string_list:
        match = pattern.search(string)
        if match:
            return match.group()
    return None


def replace_regex(sourcevar, origin, destination):
    origin_compiled = [re.compile(x, flags=re.IGNORECASE) for x in origin]
    origin_replaced = [get_first_match(x, sourcevar) for x in origin_compiled]
    out = [v if v is not None else None for i, v in enumerate(origin_replaced)]
    return out


def replace_exact(sourcevar, origin, destination):
    mapping = dict(zip(origin, destination))
    result = [mapping.get(item, None) for item in sourcevar]
    return result