import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
number = str(input("Your country code "))+str(input("Your Phonenumber "))
ch = phonenumbers.parse(number,"CH")
ser = phonenumbers.parse(number,"RO")
gb_number = phonenumbers.parse(number, "GB")
print(number)
print(timezone.time_zones_for_number(gb_number))
print(geocoder.description_for_valid_number(ch,"en"))
print(carrier.name_for_valid_number(ser,"en"))
