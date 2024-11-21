import requests

url = "https://api.chucknorris.io/jokes/random"

haku = requests.get(url).json()
print(haku["value"])
