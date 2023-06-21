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
    if isinstance(sourcevar, str):
        sourcevar = [sourcevar]
        loner = True
    else:
        loner = False

    try:
        sourcevar = [f"{x:.0f}" for x in sourcevar]
    except:
        sourcevar = [str(x).strip() for x in sourcevar]

    destination_sourcevar = data[destination]

    if origin == 'country_name':
        origin_sourcevar = [f'(?i){x}' for x in data['regex']]
    else:
        origin_sourcevar = data[origin]

    idx = [(v != 'NA') and (origin_sourcevar[i] != 'NA') for i, v in enumerate(destination_sourcevar)]

    origin_sourcevar = [v for i, v in enumerate(origin_sourcevar) if idx[i]]
    destination_sourcevar = [v for i, v in enumerate(destination_sourcevar) if idx[i]]

    dictionary = dict(zip(origin_sourcevar, destination_sourcevar))

    if origin != 'country_name':
        sourcevar_new = ["None" if x not in origin_sourcevar else x for x in sourcevar]
    else:
        sourcevar_new = copy(sourcevar)

    for k in dictionary.keys():
        sourcevar_new = [dictionary[k] if (match := re.match(f'^{k}$', x)) is not None else x for x in sourcevar_new]

    sourcevar_new = [None if x == 'None' else x for x in sourcevar_new]

    if loner:
        sourcevar_new = sourcevar_new[0]

    return sourcevar_new