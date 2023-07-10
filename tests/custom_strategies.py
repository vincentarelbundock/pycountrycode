import string
from typing import Any

from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

from countrycode import codelist


def _select_codes(code="iso3c") -> list:
    return codelist.get_column(code).drop_nulls().to_list()

def build_valid_code(code: str = "iso3c") -> SearchStrategy[str]:
    """
    Builder function that returns a strategy to pick one of a valid 'code'.
    """
    return st.sampled_from(
        _select_codes(code)
    )


def build_invalid_code(code="iso3c") -> SearchStrategy[str]:
    """
    Returns a string that is not represented in code within codelist
    """
    return st.text(alphabet=string.printable, min_size=1, max_size=10).filter(lambda z: z not in _select_codes(code))
