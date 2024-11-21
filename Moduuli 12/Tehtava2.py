import requests


def api_get(apikey, kaupunki):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={apikey}'

    vastaus = requests.get(url).json()

    saatila = vastaus["weather"][0]["main"]
    saatila_kuvaus = vastaus["weather"][0]["description"]

    lampotila = vastaus["main"]["temp"] - 273.15
    lampotila_feel = vastaus["main"]["feels_like"] - 273.15

    return ((saatila, saatila_kuvaus), (lampotila, lampotila_feel))



kaupunki = str(input("Anna kaupunki: "))

saa = api_get("0cf9396b04fe0f8508caa4ae2afb3bf8", kaupunki)

print(f'{kaupunki} sää: {saa[0][1]} \n{kaupunki} lämpötila: {int(saa[1][0])} real feal: {int(saa[1][1])}')
