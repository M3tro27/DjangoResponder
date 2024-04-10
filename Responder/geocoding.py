import requests


def get_geocordinates(address):
    access_token = "pk.eyJ1IjoiamFrdWJidmFnbmVyIiwiYSI6ImNsdTE5NHhvYTAwMTgycXJ1YXg5cTI1eXIifQ.dvd36veM8ILq0U6lusajbg"
    base_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json"
    params = {
        "access_token": access_token,
        "limit": 1
    }
    response = requests.get(base_url.format(address=address), params=params)
    data = response.json()
    if len(data['features']) > 0:
        longitude, latitude = data['features'][0]['geometry']['coordinates']
        return latitude, longitude
    else:
        return None, None
