import os
import pytest
import polars as pl
from countrycode import *

codelist = pl.read_csv("countrycode/data/codelist.csv")

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

# Test English regex vs. cldr.short.
def test_italian_regex():
    x = codelist["country.name.en"].drop_nulls()
    y = countrycode(x, origin="country.name.en", destination="cldr.short.en")
    assert (x == y).all()

# Test Italian regex vs. cldr.short.
def test_italian_regex():
    x = codelist["country.name.it"].drop_nulls()
    y = countrycode(x, origin="country.name.it", destination="cldr.short.it")
    assert (x == y).all()

# Test German regex vs. cldr.short.
def test_german_regex():
    x = codelist["country.name.de"].drop_nulls()
    y = countrycode(x, origin="country.name.de", destination="cldr.short.de")
    assert (x == y).all()

# Test French regex vs. cldr.short.
def test_french_regex():
    x = codelist["country.name.fr"].drop_nulls()
    y = countrycode(x, origin="country.name.fr", destination="cldr.short.fr")
    assert (x == y).all()