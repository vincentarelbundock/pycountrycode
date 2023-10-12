import os
import polars as pl

pkg_dir, pkg_filename = os.path.split(__file__)
pkg_dir = os.path.dirname(pkg_dir)
data_path = os.path.join(pkg_dir, "countrycode", "data", "codelist.csv")
codelist = pl.read_csv(data_path)


def test_codelist_dimensions():
    """
    Unit test to validate the dimensions of the data.
    """
    assert codelist.shape == (291, 624)
