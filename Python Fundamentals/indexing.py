import requests

# url = "https://restcountries.com/v3.1/all"

country_name = input("Please enter your country name: ")

url = f"https://restcountries.com/v3.1/name/{country_name}"

countries = requests.get(url).json()

# print(countries[0]['name']['nativeName']['spa']['common'])
# print(countries[0]['population'])

# Republic of Kenya
print(f"The population of {country_name} is: {countries[0]['population']}")
