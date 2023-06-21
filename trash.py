from countrycode.countrycode import *
k = countrycode(['canada', 'united states', 'alGeria'], origin = "country.name.en.regex", destination = "iso3c")

gg

countrycode(['DZA', 'CAN', 'USA'], origin = "iso3c", destination = "cldr.short.fr")
countrycode(['DZA', 'CAN', 'USA'], origin = "iso3c", destination = "iso3n")

# TODO: numeric codes should not be strings
# probably due to my dict reading
countrycode(['12', '124'], origin = "iso3n", destination = "cldr.short.fr")


origin = [
'zambia|northern.?rhodesia',
'^(?!south)(?!republic).*viet.?nam(?!.*south)|democratic.republic.of.vietnam|socialist.republic.of.viet.?nam|north.viet.?nam|viet.?nam.north'
]
sourcevar = ["Democratic Republic of Vietnam", "Algeria"]
destination = ["Zambia", "Vietnam"]

replace_regex(sourcevar, origin, ["Zambia", "Vietnam"])


origin_compiled = [re.compile(x, flags=re.IGNORECASE) for x in origin]
origin_replaced = [get_first_match(x, sourcevar) for x in origin_compiled]
out = replace_exact(origin, origin_replaced, destination)

replace_regex(sourcevar, origin, ["Zambia", "Vietnam"])

origin_compiled = [re.compile(x, flags=re.IGNORECASE) for x in origin]
origin_replaced = [get_first_match(x, sourcevar) for x in o]
out = replace_exact(origin, origin_replaced, destination)

re.search(origin[1], "Democratic Republic of Vietnam")