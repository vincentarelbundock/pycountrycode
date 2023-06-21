from countrycode.countrycode import countrycode

countrycode(['DZA', 'CAN', 'USA'], origin = "iso3c", destination = "cldr.short.en")

countrycode(['Canada', 'United States'], origin = "country.name.en.regex", destination = "iso3c", origin_regex = True)
