# python -m pip --upgrade pip

import requests
from bs4 import BeautifulSoup
import json

# response = requests.get('https://norvig.com')
# print(response.text)

# url = 'https://norvig.com'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# # remove all the HTML tags
# text = soup.get_text()
# print(text)

url = 'https://restcountries.com/v3.1/all'
response = requests.get(url)
print(len(response.json()))

for country in response.json():
    if country['name']['common'] == 'Canada':
        # print(f'country[\'name\'][\'common\'] is {country["name"]["common"]}\n')
        # print(json.dumps(country))
        print(country.get('coatOfArms').get('png'))


