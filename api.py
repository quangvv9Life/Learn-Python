import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

print(source)

data = json.loads(source)

# print(len(data['list'['resources']]))

usd_rates = dict() #create a dictionary in python from json data

for item in data['list']['resources']:
    # print(item)
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    # print(name, price)
    usd_rates[name] = price #dictionary usr_rates with name as the key and price is value

print(usd_rates['USD/EUR'])
