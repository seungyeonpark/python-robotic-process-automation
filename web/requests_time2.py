import requests
from _MyPath import URL

url = URL + 'today'
response = requests.get(url)

print("type = ", type(response))

print("ok = ", response.ok)

if response.ok:
    print("text = ", response.text)

print("status_code = ", response.status_code)
