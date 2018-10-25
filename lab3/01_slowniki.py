# Zadanie: pobrac definicje slowa, zapisywac ja w slowniku i potem ewentualnie na dysku
import requests
import json
import sys

filename = "slownik.json"

app_id = '4243f055' # zamienić na prywatne app_id
app_key = '31b1849215c0b99c6d0d6b18d7abf7e6' # zamienić na prywatne app_key

language = 'en'

mydict = {}
try:
    dictfile = open(filename, "a+") # taki hack, jakby pliku nie było
    dictfile.close()

    dictfile = open(filename, "r+")
    dictdata = dictfile.read()
    try:
        mydict = json.loads(dictdata)
        print("File opened successfully")
    except json.decoder.JSONDecodeError:
        print("Could not load data from file")
    dictfile.close()
    while True:
        print("\n" + str(len(mydict.keys())) + " words available offline")
        for key in mydict.keys():
            print(key, end=", ")
        print(" ")
        word_id = input("Enter a word (Ctrl+C to save and exit): ")
        if not word_id.lower() in mydict.keys():
            url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
            r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
            if r.status_code == 200:
                data = r.json()
                definitions = []
                print("Definitions for \"" + word_id + "\":")
                if (data is not None) and ("results" in data):
                    for result in data["results"]:
                        for lexEntries in result["lexicalEntries"]:
                            for entry in lexEntries["entries"]:
                                for sense in entry["senses"]:
                                    if "definitions" in sense:
                                        for definition in sense["definitions"]:
                                            definitions.append(definition)
                                            print("- " + definition, end="\n")

                    mydict[word_id.lower()] = definitions
                else:
                    print("Word \"" + word_id + "\" could not be found")
            else:
                print("Word \"" + word_id + "\" could not be found")
        else:
            print("Definitions for \"" + word_id + "\": ")
            for definition in mydict[word_id.lower()]:
                print("- " + definition)

except KeyboardInterrupt:
    dictfile = open(filename, "w+")
    dictfile.write(json.dumps(mydict))
    dictfile.close()
    sys.exit()