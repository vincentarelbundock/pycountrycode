from countrycode.countrycode import *
countrycode(['canada', 'United States', 'alGeria'], origin = "country.name.en.regex", destination = "iso3c")
countrycode(pl.Series(['DZA', 'CAN', 'USA']), origin = "iso3c", destination = "cldr.short.fr")
countrycode(['DZA', 'CAN', 'USA'], origin = "iso3c", destination = "iso3n")
countrycode([12, 124], origin = "iso3n", destination = "cldr.short.fr")
countrycode(12, origin = "iso3n", destination = "cldr.short.de") 
countrycode(["Democratic Republic of Vietnam", "Algeria"], origin = "country.name.en.regex", destination = "iso3c")