import os
import pytest

from hypothesis import given, example

from countrycode import countrycode

try:
    from custom_strategies_polars import (
        build_valid_code as build_valid_code_polars,
        select_filtered_row as select_filtered_row_polars
    )

    _has_polars = True

    pkg_dir, pkg_filename = os.path.split(__file__)
    pkg_dir = os.path.dirname(pkg_dir)
    data_path = os.path.join(pkg_dir, "countrycode", "data", "codelist.csv")
    codelist = pl.read_csv(data_path)

except ImportError:
    _has_polars = False
    from custom_strategies import codelist

_regex_internal_skip_reason = "Test requires polars installation"

"""
Test to check that finding the iso3n representation of an iso3c row is
equivalent to finding the corresponding cell in the countrycode dataframe.
"""





def test_basic_conversions():
    def name_of(iso3c_code):
        return countrycode(iso3c_code, origin='iso3c', destination='country.name')

    assert name_of('CAN') == 'Canada'
    assert name_of(['USA', 'CAN']) == ['United States', 'Canada']


def test_issue_252():
    assert countrycode("United States", "country.name", "p5c") == "USA"
    assert countrycode("United States", "country.name", "p5n") == 2


def test_invalid_iso3c_to_country_name():
    def name_of(iso3c_code):
        return countrycode(iso3c_code, 'iso3c', 'country.name')

    assert name_of('BAD') is None
    assert name_of(['BAD', 'BLA', 'CAN']) == [None, None, 'Canada']
