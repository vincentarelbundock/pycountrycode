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

def countrycode(sourcevar=['DZA', 'CAN'], origin='iso3c', destination='country.name.en', origin_regex = False):

    # sanity checks
    if origin not in data.keys():
        raise ValueError(f"origin {origin} not found in the code list.")
    else:
        origin = data[origin]

    if destination not in data.keys():
        raise ValueError(f"destination {destination} not found in the code list.")
    else:
        destination = data[destination]


    if isinstance(sourcevar, str):
        sourcevar = [sourcevar]
        loner = True
    else:
        loner = False

    mapping = dict(zip(origin, destination))

    if origin_regex:
        out = replace_regex(sourcevar, mapping)
    else:
        out = replace_exact(sourcevar, mapping)

    # TODO: sanitize input
    # white space only if string
    # sourcevar = [str(x).strip() for x in sourcevar]
    # round numeric if
    # sourcevar = [f"{x:.0f}" for x in sourcevar]

    if loner:
        out = out[0]

    return out


def replace_exact(sourcevar, mapping):
    result = [mapping.get(item, None) for item in sourcevar]
    return result

def replace_regex(sourcevar, mapping):
    result = []
    for item in sourcevar:
        replaced = False
        for pattern, replacement in mapping.items():
            if re.search(pattern, item):
                result.append(re.sub(pattern, replacement, item))
                replaced = True
                break
        if not replaced:
            result.append(None)

    return result