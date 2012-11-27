#!/usr/bin/env python
'''
    Created Jul 23, 2011.
    Reads a country code and returns the name of the country.
    Author: Sam Gleske
'''
class CountryCodes:
  """
  Reads a country code and returns the name of the country.

  Usage: 
  from CountryCodes import CountryCodes
  print CountryCodes("US").country
  """
  ccodeList = [
      ("AD","Andorra"),
      ("AE","Arab Emirates"),
      ("AG","Antigua And Barbuda"),
      ("AI","Anguilla"),
      ("AL","Albania"),
      ("AM","Armenia"),
      ("AN","Neth. Antilles"),
      ("AO","Angola"),
      ("AR","Argentina"),
      ("AT","Austria"),
      ("AU","Australia"),
      ("AW","Aruba"),
      ("AZ","Azerbaijan"),
      ("BA","Bosnia And Herzegovina"),
      ("BB","Barbados"),
      ("BD","Bangladesh"),
      ("BE","Belgium"),
      ("BG","Bulgaria"),
      ("BH","Bahrain"),
      ("BM","Bermuda"),
      ("BN","Brunei"),
      ("BO","Bolivia"),
      ("BR","Brazil"),
      ("BS","The Bahamas"),
      ("BW","Botswana"),
      ("BY","Belarus"),
      ("BZ","Belize"),
      ("CA","Canada"),
      ("CC","Cocos Islands"),
      ("CD","Congo, Democratic Republic Of"),
      ("CH","Switzerland"),
      ("CI","Ivory Coast"),
      ("CK","Cook Islands"),
      ("CL","Chile"),
      ("CM","Cameroon"),
      ("CN","China P.Rep."),
      ("CO","Colombia"),
      ("CR","Costa Rica"),
      ("CS","Czechoslovakia"),
      ("CU","Cuba"),
      ("CY","Cyprus"),
      ("CZ","Czech Republic"),
      ("DE","Germany"),
      ("DK","Denmark"),
      ("DM","Dominica"),
      ("DO","Dominican Repl."),
      ("DZ","Algeria"),
      ("EC","Ecuador"),
      ("EE","Estonia"),
      ("EG","Egypt"),
      ("ES","Spain"),
      ("ET","Ethiopia"),
      ("FI","Finland"),
      ("FJ","Fiji"),
      ("FK","Falkland Islands (Malvinas)"),
      ("FO","Faroe Islands"),
      ("FR","France"),
      ("GA","Gabon"),
      ("GB","United Kingdom"),
      ("GD","Grenada"),
      ("GE","Georgia (Republic Of)"),
      ("GF","French Guiana"),
      ("GH","Ghana"),
      ("GI","Gibraltar"),
      ("GL","Greenland"),
      ("GM","Gambia"),
      ("GN","Guinea"),
      ("GP","Guadeloupe"),
      ("GR","Greece"),
      ("GT","Guatemala"),
      ("GY","Guyana"),
      ("HK","China,Hong Kong S.A.R."),
      ("HN","Honduras"),
      ("HR","Croatia"),
      ("HT","Haiti"),
      ("HU","Hungary"),
      ("ID","Indonesia"),
      ("IE","Ireland"),
      ("IL","Israel"),
      ("IN","India"),
      ("IQ","Iraq"),
      ("IR","Iran"),
      ("IS","Iceland"),
      ("IT","Italy"),
      ("JM","Jamaica"),
      ("JO","Jordan"),
      ("JP","Japan"),
      ("KE","Kenya"),
      ("KG","Kyrgyzstan"),
      ("KH","Cambodia"),
      ("KN","Saint Kitts And Nevis"),
      ("KP","North Korea"),
      ("KR","South Korea"),
      ("KW","Kuwait"),
      ("KY","Cayman Islands"),
      ("KZ","Kazakhstan"),
      ("LA","Laos"),
      ("LB","Lebanon"),
      ("LC","St. Lucia"),
      ("LI","Liechtenstein"),
      ("LK","Sri Lanka"),
      ("LR","Liberia"),
      ("LT","Lithuania"),
      ("LU","Luxembourg"),
      ("LV","Latvia"),
      ("LY","Libya"),
      ("MA","Morocco"),
      ("MC","Monaco"),
      ("MD","Moldova, Republic Of"),
      ("MG","Madagascar"),
      ("MH","Marshall Islands"),
      ("MK","Macedonia, Former Yugoslav Rep."),
      ("ML","Mali"),
      ("MM","Myanmar"),
      ("MO","Macau"),
      ("MQ","Martinique"),
      ("MR","Mauritania"),
      ("MT","Malta"),
      ("MU","Mauritius"),
      ("MW","Malawi"),
      ("MX","Mexico"),
      ("MY","Malaysia"),
      ("MZ","Mozambique"),
      ("NA","Namibia"),
      ("NC","New Caledonia"),
      ("NE","Niger"),
      ("NF","Norfolk Island"),
      ("NG","Nigeria"),
      ("NI","Nicaragua"),
      ("NL","Netherlands"),
      ("NO","Norway"),
      ("NP","Nepal"),
      ("NZ","New Zealand"),
      ("OM","Oman"),
      ("PA","Panama"),
      ("PE","Peru"),
      ("PF","Fr. Polynesia"),
      ("PG","New Guinea"),
      ("PH","Philippines"),
      ("PK","Pakistan"),
      ("PL","Poland"),
      ("PR","Puerto Rico"),
      ("PT","Portugal"),
      ("PW","Palau"),
      ("PY","Paraguay"),
      ("QA","Qatar"),
      ("RO","Romania"),
      ("RU","Russian Federation"),
      ("SA","Saudi Arabia"),
      ("SB","Solomon Islands"),
      ("SD","Sudan"),
      ("SE","Sweden"),
      ("SG","Singapore"),
      ("SI","Slovenia"),
      ("SK","Slovakia"),
      ("SL","Sierra Leone"),
      ("SM","San Marino"),
      ("SN","Senegal"),
      ("SR","Suriname"),
      ("SU","U.S.S.R."),
      ("SV","El Salvador"),
      ("SY","Syria"),
      ("SZ","Swaziland"),
      ("TC","Turks And Caicos Islands"),
      ("TD","Chad"),
      ("TH","Thailand"),
      ("TN","Tunisia"),
      ("TR","Turkey"),
      ("TT","Trinidad/Tobago"),
      ("TW","Taiwan"),
      ("TZ","Tanzania"),
      ("UA","Ukraine"),
      ("UG","Uganda"),
      ("US","United States"),
      ("UY","Uruguay"),
      ("UZ","Uzbekistan"),
      ("VA","Vatican City State (Holy See)"),
      ("VC","St. Vincent/Grenadines"),
      ("VE","Venezuela"),
      ("VG","Virgin (British) Islands"),
      ("VN","Viet Nam"),
      ("VU","Vanuatu (New Hebrides)"),
      ("YE","Yemen"),
      ("YU","Yugoslavia"),
      ("ZA","South Africa"),
      ("ZM","Zambia"),
      ("ZW","Zimbabwe")
    ]
  country = ""
  def __init__(self, ccode = ""):
    for country in self.ccodeList:
      if country[0] == ccode.upper():
        self.country = country[1]
        break
      else:
        self.country = "Country Unknown (" + ccode + ")"