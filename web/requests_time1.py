import requests
from _MyPath import URL

url = URL + 'today'
response = requests.get(url)

print(response.text)
