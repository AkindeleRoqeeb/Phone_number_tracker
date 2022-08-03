import phonenumbers

from my_number import Number

from phonenumbers import geocoder

some_num = phonenumbers.parse(Number)

yourlocation = geocoder.description_for_number(some_num, "en")
print(yourlocation)