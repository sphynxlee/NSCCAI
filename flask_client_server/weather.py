import requests

city_address = 'halifax'
city_url  = f'https://geocode.maps.co/search?q={city_address}'
city_response = requests.get(city_url)
if city_response.status_code != 200:
    print(f'error: {city_response.status_code}')
    exit(1)

city_data = city_response.json()
# print(f'city_data: {city_data}')
city_json = {"lat": city_data[0]["lat"], "lon": city_data[0]["lon"]}
print(f'city_json: {city_json}')


weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={city_json["lat"]}&longitude={city_json["lon"]}&current=temperature_2m,windspeed_10m&hourly=temperature_2m,relativehumidity_2m,windspeed_10m'
print(f'weather_url: {weather_url}')

weather_response = requests.get(weather_url)
if weather_response.status_code != 200:
    print(f'error: {weather_response.status_code}')
    exit(1)

weather_data = weather_response.json()
print(f'weather_data: {weather_data}')

