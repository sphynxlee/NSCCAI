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

fh = open('countries.txt', 'w', encoding='utf-8')
fh.write(response.text)

for country in response.json():
    if country['name']['common'] == 'Canada':
        # print(f'country[\'name\'][\'common\'] is {country["name"]["common"]}\n')
        # print(json.dumps(country))
        print(country.get('coatOfArms').get('png'))
        coat_of_arms = country.get('coatOfArms').get('png')
        coat_of_arms = country['coatOfArms']['png']
        coa = requests.get(coat_of_arms)
        bfh = open('coat_of_arms.png', 'wb')
        bfh.write(coa.content)


