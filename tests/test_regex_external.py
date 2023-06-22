import pytest
from countrycode import countrycode

def iso3c_of(name): 
    out = countrycode(sourcevar = name, origin = 'country.name', destination = 'iso3c')
    if out is None:
        out = ""
    return out

def test_known_variants():

    assert iso3c_of('Aruba') == 'ABW'
    assert iso3c_of('Afghanistan') == 'AFG'
    assert iso3c_of('Angola') == 'AGO'
    assert iso3c_of('Anguilla') == 'AIA'
    assert iso3c_of('åland Islands') == 'ALA'
    assert iso3c_of('Albania') == 'ALB'
    assert iso3c_of('Andorra') == 'AND'
    assert iso3c_of('United Arab Emirates') == 'ARE'
    assert iso3c_of('Argentina') == 'ARG'
    assert iso3c_of('Armenia') == 'ARM'
    assert iso3c_of('American Samoa') == 'ASM'
    assert iso3c_of('Antarctica') == 'ATA'
    assert iso3c_of('French Southern and Antarctic Lands') == 'ATF'
    assert iso3c_of('Antigua and Barbuda') == 'ATG'
    assert iso3c_of('Australia') == 'AUS'
    assert iso3c_of('Austria') == 'AUT'
    assert iso3c_of('Azerbaijan') == 'AZE'
    assert iso3c_of('Burundi') == 'BDI'
    assert iso3c_of('Belgium') == 'BEL'
    assert iso3c_of('Benin') == 'BEN'
    assert iso3c_of('Caribbean Netherlands') == 'BES'
    assert iso3c_of('Burkina Faso') == 'BFA'
    assert iso3c_of('Bangladesh') == 'BGD'
    assert iso3c_of('Bulgaria') == 'BGR'
    assert iso3c_of('Bahrain') == 'BHR'
    assert iso3c_of('The Bahamas') == 'BHS'
    assert iso3c_of('Bosnia and Herzegovina') == 'BIH'
    assert iso3c_of('Saint Barth\u00E9lemy') == 'BLM'
    assert iso3c_of('Belarus') == 'BLR'
    assert iso3c_of('Belize') == 'BLZ'
    assert iso3c_of('Bermuda') == 'BMU'
    assert iso3c_of('Bolivia') == 'BOL'
    assert iso3c_of('Brazil') == 'BRA'
    assert iso3c_of('Barbados') == 'BRB'
    assert iso3c_of('Brunei') == 'BRN'
    assert iso3c_of('Bhutan') == 'BTN'
    assert iso3c_of('Bouvet Island') == 'BVT'
    assert iso3c_of('Botswana') == 'BWA'
    assert iso3c_of('Central African Republic') == 'CAF'
    assert iso3c_of('Canada') == 'CAN'
    assert iso3c_of('Cocos (Keeling) Islands') == 'CCK'
    assert iso3c_of('Switzerland') == 'CHE'
    assert iso3c_of('Chile') == 'CHL'
    assert iso3c_of('China') == 'CHN'
    assert iso3c_of('C\u00F4te d\'Ivoire') == 'CIV'
    assert iso3c_of('Cameroon') == 'CMR'
    assert iso3c_of('Democratic Republic of the Congo') == 'COD'
    assert iso3c_of('Republic of the Congo') == 'COG'
    assert iso3c_of('Cook Islands') == 'COK'
    assert iso3c_of('Colombia') == 'COL'
    assert iso3c_of('Comoros') == 'COM'
    assert iso3c_of('Cabo Verde') == 'CPV'
    assert iso3c_of('Costa Rica') == 'CRI'
    assert iso3c_of('Cuba') == 'CUB'
    assert iso3c_of('Cura\u00E7ao') == 'CUW'
    assert iso3c_of('Christmas Island') == 'CXR'
    assert iso3c_of('Cayman Islands') == 'CYM'
    assert iso3c_of('Cyprus') == 'CYP'
    assert iso3c_of('Czech Republic') == 'CZE'
    assert iso3c_of('Germany') == 'DEU'
    assert iso3c_of('Djibouti') == 'DJI'
    assert iso3c_of('Dominica') == 'DMA'
    assert iso3c_of('Denmark') == 'DNK'
    assert iso3c_of('Dominican Republic') == 'DOM'
    assert iso3c_of('Algeria') == 'DZA'
    assert iso3c_of('Ecuador') == 'ECU'
    assert iso3c_of('Egypt') == 'EGY'
    assert iso3c_of('Eritrea') == 'ERI'
    assert iso3c_of('Western Sahara') == 'ESH'
    assert iso3c_of('Spain') == 'ESP'
    assert iso3c_of('Estonia') == 'EST'
    assert iso3c_of('Ethiopia') == 'ETH'
    assert iso3c_of('Finland') == 'FIN'
    assert iso3c_of('Fiji') == 'FJI'
    assert iso3c_of('Falkland Islands') == 'FLK'
    assert iso3c_of('France') == 'FRA'
    assert iso3c_of('Faroe Islands') == 'FRO'
    assert iso3c_of('Federated States of Micronesia') == 'FSM'
    assert iso3c_of('Gabon') == 'GAB'
    assert iso3c_of('United Kingdom') == 'GBR'
    assert iso3c_of('Georgia') == 'GEO'
    assert iso3c_of('Guernsey') == 'GGY'
    assert iso3c_of('Ghana') == 'GHA'
    assert iso3c_of('Gibraltar') == 'GIB'
    assert iso3c_of('Guinea') == 'GIN'
    assert iso3c_of('Guadeloupe') == 'GLP'
    assert iso3c_of('The Gambia') == 'GMB'
    assert iso3c_of('Guinea-Bissau') == 'GNB'
    assert iso3c_of('Equatorial Guinea') == 'GNQ'
    assert iso3c_of('Greece') == 'GRC'
    assert iso3c_of('Grenada') == 'GRD'
    assert iso3c_of('Greenland') == 'GRL'
    assert iso3c_of('Guatemala') == 'GTM'
    assert iso3c_of('French Guiana') == 'GUF'
    assert iso3c_of('Guam') == 'GUM'
    assert iso3c_of('Guyana') == 'GUY'
    assert iso3c_of('Hong Kong') == 'HKG'
    assert iso3c_of('Heard Island and McDonald Islands') == 'HMD'
    assert iso3c_of('Honduras') == 'HND'
    assert iso3c_of('Croatia') == 'HRV'
    assert iso3c_of('Haiti') == 'HTI'
    assert iso3c_of('Hungary') == 'HUN'
    assert iso3c_of('Indonesia') == 'IDN'
    assert iso3c_of('Isle of Man') == 'IMN'
    assert iso3c_of('India') == 'IND'
    assert iso3c_of('British Indian Ocean Territory') == 'IOT'
    assert iso3c_of('Republic of Ireland') == 'IRL'
    assert iso3c_of('Iran') == 'IRN'
    assert iso3c_of('Iraq') == 'IRQ'
    assert iso3c_of('Iceland') == 'ISL'
    assert iso3c_of('Israel') == 'ISR'
    assert iso3c_of('Italy') == 'ITA'
    assert iso3c_of('Jamaica') == 'JAM'
    assert iso3c_of('Jersey') == 'JEY'
    assert iso3c_of('Jordan') == 'JOR'
    assert iso3c_of('Japan') == 'JPN'
    assert iso3c_of('Kazakhstan') == 'KAZ'
    assert iso3c_of('Kenya') == 'KEN'
    assert iso3c_of('Kyrgyzstan') == 'KGZ'
    assert iso3c_of('Cambodia') == 'KHM'
    assert iso3c_of('Kiribati') == 'KIR'
    assert iso3c_of('Saint Kitts and Nevis') == 'KNA'
    assert iso3c_of('South Korea') == 'KOR'
    assert iso3c_of('Kuwait') == 'KWT'
    assert iso3c_of('Laos') == 'LAO'
    assert iso3c_of('Lebanon') == 'LBN'
    assert iso3c_of('Liberia') == 'LBR'
    assert iso3c_of('Libya') == 'LBY'
    assert iso3c_of('Saint Lucia') == 'LCA'
    assert iso3c_of('Liechtenstein') == 'LIE'
    assert iso3c_of('Sri Lanka') == 'LKA'
    assert iso3c_of('Lesotho') == 'LSO'
    assert iso3c_of('Lithuania') == 'LTU'
    assert iso3c_of('Luxembourg') == 'LUX'
    assert iso3c_of('Latvia') == 'LVA'
    assert iso3c_of('Macau') == 'MAC'
    assert iso3c_of('Collectivity of Saint Martin') == 'MAF'
    assert iso3c_of('Morocco') == 'MAR'
    assert iso3c_of('Monaco') == 'MCO'
    assert iso3c_of('Moldova') == 'MDA'
    assert iso3c_of('Madagascar') == 'MDG'
    assert iso3c_of('Maldives') == 'MDV'
    assert iso3c_of('Mexico') == 'MEX'
    assert iso3c_of('Marshall Islands') == 'MHL'
    assert iso3c_of('Republic of Macedonia') == 'MKD'
    assert iso3c_of('Mali') == 'MLI'
    assert iso3c_of('Malta') == 'MLT'
    assert iso3c_of('Myanmar') == 'MMR'
    assert iso3c_of('Montenegro') == 'MNE'
    assert iso3c_of('Mongolia') == 'MNG'
    assert iso3c_of('Northern Mariana Islands') == 'MNP'
    assert iso3c_of('Mozambique') == 'MOZ'
    assert iso3c_of('Mauritania') == 'MRT'
    assert iso3c_of('Montserrat') == 'MSR'
    assert iso3c_of('Martinique') == 'MTQ'
    assert iso3c_of('Mauritius') == 'MUS'
    assert iso3c_of('Malawi') == 'MWI'
    assert iso3c_of('Malaysia') == 'MYS'
    assert iso3c_of('Mayotte') == 'MYT'
    assert iso3c_of('Namibia') == 'NAM'
    assert iso3c_of('New Caledonia') == 'NCL'
    assert iso3c_of('Niger') == 'NER'
    assert iso3c_of('Norfolk Island') == 'NFK'
    assert iso3c_of('Nigeria') == 'NGA'
    assert iso3c_of('Nicaragua') == 'NIC'
    assert iso3c_of('Niue') == 'NIU'
    assert iso3c_of('Netherlands') == 'NLD'
    assert iso3c_of('Norway') == 'NOR'
    assert iso3c_of('Nepal') == 'NPL'
    assert iso3c_of('Nauru') == 'NRU'
    assert iso3c_of('New Zealand') == 'NZL'
    assert iso3c_of('Oman') == 'OMN'
    assert iso3c_of('Pakistan') == 'PAK'
    assert iso3c_of('Panama') == 'PAN'
    assert iso3c_of('Pitcairn Islands') == 'PCN'
    assert iso3c_of('Peru') == 'PER'
    assert iso3c_of('Philippines') == 'PHL'
    assert iso3c_of('Palau') == 'PLW'
    assert iso3c_of('Papua New Guinea') == 'PNG'
    assert iso3c_of('Poland') == 'POL'
    assert iso3c_of('Puerto Rico') == 'PRI'
    assert iso3c_of('North Korea') == 'PRK'
    assert iso3c_of('Portugal') == 'PRT'
    assert iso3c_of('Paraguay') == 'PRY'
    assert iso3c_of('State of Palestine') == 'PSE'
    assert iso3c_of('French Polynesia') == 'PYF'
    assert iso3c_of('Qatar') == 'QAT'
    assert iso3c_of('R\u00E9union') == 'REU'
    assert iso3c_of('Romania') == 'ROU'
    assert iso3c_of('Russia') == 'RUS'
    assert iso3c_of('Rwanda') == 'RWA'
    assert iso3c_of('Saudi Arabia') == 'SAU'
    assert iso3c_of('Sudan') == 'SDN'
    assert iso3c_of('Senegal') == 'SEN'
    assert iso3c_of('Singapore') == 'SGP'
    assert iso3c_of('South Georgia and the South Sandwich Islands') == 'SGS'
    assert iso3c_of('Saint Helena == Ascension and Tristan da Cunha') == 'SHN'
    assert iso3c_of('Svalbard and Jan Mayen') == 'SJM'
    assert iso3c_of('Solomon Islands') == 'SLB'
    assert iso3c_of('Sierra Leone') == 'SLE'
    assert iso3c_of('El Salvador') == 'SLV'
    assert iso3c_of('San Marino') == 'SMR'
    assert iso3c_of('Somalia') == 'SOM'
    assert iso3c_of('Saint Pierre and Miquelon') == 'SPM'
    assert iso3c_of('Serbia') == 'SRB'
    assert iso3c_of('South Sudan') == 'SSD'
    assert iso3c_of('S\u00E3o Tom\u00E9 and Pr\u00EDncipe') == 'STP'
    assert iso3c_of('Suriname') == 'SUR'
    assert iso3c_of('Slovakia') == 'SVK'
    assert iso3c_of('Slovenia') == 'SVN'
    assert iso3c_of('Sweden') == 'SWE'
    assert iso3c_of('Swaziland') == 'SWZ'
    assert iso3c_of('Sint Maarten') == 'SXM'
    assert iso3c_of('Seychelles') == 'SYC'
    assert iso3c_of('Syria') == 'SYR'
    assert iso3c_of('Turks and Caicos Islands') == 'TCA'
    assert iso3c_of('Chad') == 'TCD'
    assert iso3c_of('Togo') == 'TGO'
    assert iso3c_of('Thailand') == 'THA'
    assert iso3c_of('Tajikistan') == 'TJK'
    assert iso3c_of('Tokelau') == 'TKL'
    assert iso3c_of('Turkmenistan') == 'TKM'
    assert iso3c_of('East Timor') == 'TLS'
    assert iso3c_of('Tonga') == 'TON'
    assert iso3c_of('Trinidad and Tobago') == 'TTO'
    assert iso3c_of('Tunisia') == 'TUN'
    assert iso3c_of('Turkey') == 'TUR'
    assert iso3c_of('Tuvalu') == 'TUV'
    assert iso3c_of('Taiwan') == 'TWN'
    assert iso3c_of('Tanzania') == 'TZA'
    assert iso3c_of('Uganda') == 'UGA'
    assert iso3c_of('Ukraine') == 'UKR'
    assert iso3c_of('United States Minor Outlying Islands') == 'UMI'
    assert iso3c_of('Uruguay') == 'URY'
    assert iso3c_of('United States') == 'USA'
    assert iso3c_of('Uzbekistan') == 'UZB'
    assert iso3c_of('Vatican City') == 'VAT'
    assert iso3c_of('Saint Vincent and the Grenadines') == 'VCT'
    assert iso3c_of('Venezuela') == 'VEN'
    assert iso3c_of('British Virgin Islands') == 'VGB'
    assert iso3c_of('United States Virgin Islands') == 'VIR'
    assert iso3c_of('Viet Nam') == 'VNM'
    assert iso3c_of('Vanuatu') == 'VUT'
    assert iso3c_of('Wallis and Futuna') == 'WLF'
    assert iso3c_of('Samoa') == 'WSM'
    assert iso3c_of('Yemen') == 'YEM'
    assert iso3c_of('South Africa') == 'ZAF'
    assert iso3c_of('Zambia') == 'ZMB'
    assert iso3c_of('Zimbabwe') == 'ZWE'
