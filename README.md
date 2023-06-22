# Python countrycode

Convert country names to and from 9 country code schemes.

- Bugs & Development:
  https://github.com/vincentarelbundock/pycountrycode
- Pypi: https://pypi.python.org/pypi/countrycode
- `Vincent's webpage <http://umich.edu/~varel>`\_

A Python port of the `countrycode` package for R:

- `countrycode @ Github <http://github.com/vincentarelbundock/countrycode>`\_
- `countrycode @ CRAN <http://cran.r-project.org/web/packages/countrycode/index.html>`\_

This is *beta* software.

# Installation

Using pip

``` python
sudo pip install countrycode
```

Latest version from Gitub

``` {sh}
#| eval: false
git clone https://github.com/vincentarelbundock/pycountrycode
cd pycountrycode
pip install .
```

# Usage

``` python
from countrycode import countrycode
countrycode(['Algeria', 'United States'], origin='country.name', destination='iso3c')
```

    ['DZA', 'USA']
