import pytest
import polars as pl
from countrycode.countrycode import *

# Test all country names with iso3c codes are matched exactly once
def test_iso3c_match():
    name = codelist.filter(pl.col("iso3c").is_not_null())["country.name.en"]
    iso3c_from_name = countrycode(name, origin='country.name', destination = "iso3c")
    assert len(iso3c_from_name) == len(set(iso3c_from_name))

# Test iso3c-to-country.name-to-iso3c is internally consistent
def test_iso3c_consistency():
    for iso3c_original in codelist["iso3c"].drop_nulls():
        if iso3c_original is not None:
            name = countrycode(iso3c_original, origin='iso3c', destination='cldr.short.en')
            iso3c_result = countrycode(name, origin = "country.name", destination = "iso3c")
            assert iso3c_result == iso3c_original

# # Test Italian regex vs. CLDR
# def test_italian_regex():
#     x = coco.CountryConverter().convert(codelist["country.name.it"], from_="name_short", to="CLDR")
#     assert (x == codelist["cldr.name.it"]).all()

# # Test German regex vs. CLDR
# def test_german_regex():
#     x = coco.CountryConverter().convert(codelist["country.name.de"], from_="name_short", to="CLDR")
#     assert (x == codelist["cldr.name.de"]).all()

# # Test French regex vs. CLDR
# def test_french_regex():
#     x = coco.CountryConverter().convert(codelist["country.name.fr"], from_="name_short", to="CLDR")
#     assert (x == codelist["cldr.name.fr"]).all()