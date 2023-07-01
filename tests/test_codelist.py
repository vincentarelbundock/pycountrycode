from countrycode import codelist


def test_codelist_dimensions():
    """
    Unit test to validate the dimensions of the data.
    """
    assert codelist.shape == (291, 624)
