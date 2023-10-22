from countrycode import countrycode

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
