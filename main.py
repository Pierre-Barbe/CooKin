import requests

# City name import
city = input('Please input the city name : ')

# Corresponding wttr.in url for selected city
url = 'https://wttr.in/{}'.format(city)

# Weather ASCII answer from wttr url request
weather_res = requests.get(url)

print(weather_res.text)