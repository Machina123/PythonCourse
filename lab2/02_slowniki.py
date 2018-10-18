# ------- SŁOWNIKI --------
# Definicja slownika:
# dict = {key1: value1, key2: value2, ...}
#
# Wpisanie wartosci do slownika:
# dict[key3] = value3
#
# Wypisywanie wartosci pod danym kluczem:
# print dict[key3]
#
# iterowanie po kluczach:
# for k in keys(dict): ...
# [LUB]
# for key,value in dict: ...
#
# ZADANIE:
# pobieranie danych ze słownika Oxford
# i dopisywanie danych do lokalnego słownika (jako cache)
# później: zapisywanie słownika do pliku i późniejsze odczytanie 
# co by nie marnować zapytań do API

# skopiowane z przykładów

import requests
import json

app_id = '4243f055' # zamienić na prywatne app_id
app_key = '31b1849215c0b99c6d0d6b18d7abf7e6' # zamienić na prywatne app_key

language = 'en'
word_id = 'Ace'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))