import phonenumbers
from pyfiglet import figlet_format

print(figlet_format("NumberTrack", font = "standard" ))


number = input("Enter number:")

print("The following number is being processed "+number)

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_prov = phonenumbers.parse(number, "SP")
print(carrier.name_for_number(service_prov, "en"))

