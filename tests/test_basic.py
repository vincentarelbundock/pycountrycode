import pytest
from countrycode import countrycode


def test_numeric():
    assert countrycode("CAN", "iso3c", "iso3n") == 124


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
