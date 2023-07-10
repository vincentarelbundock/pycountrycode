from hypothesis import given, example

from countrycode import countrycode, codelist
from custom_strategies import build_invalid_code, build_valid_code
import polars as pl


@given(build_valid_code("iso3c"))
@example(code_param="AFG")
def test_iso3c_conversion(code_param):
    expected = codelist.filter(pl.col("iso3c") == code_param).item(0, "country.name.en")
    assert countrycode(code_param, "iso3c", 'country.name') == expected


@given(build_invalid_code("iso3c"))
def test_iso3c_invalid_conversion(code):
    assert countrycode(code, "iso3c", 'country.name') is None
