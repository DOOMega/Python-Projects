import requests
import json


API_key = "23aafa1e21c4739bef3b6266"
API_url = f"https://v6.exchangerate-api.com/v6/{API_key}/latest/USD"

bozulan_döviz = input("bozulan döviz türü: ")
alınan_döviz = input("alınan döviz türü: ")
miktar = input(f"ne kadar {bozulan_döviz} bozdurmak istiyorsunuz: ")

sonuç = requests.get(API_url + bozulan_döviz)
sonuç_json = json.loads(sonuç.text)

print(sonuç_json["conversion_rates"][alınan_döviz])