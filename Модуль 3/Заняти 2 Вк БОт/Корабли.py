import requests

url = "https://swapi.dev/api/vehicles/"

def starships(url):
    response_starships = requests.get(url).json()
    for i in response_starships['results']:

        print(i['name'])
        print(i['max_atmosphering_speed'])


starships(url)