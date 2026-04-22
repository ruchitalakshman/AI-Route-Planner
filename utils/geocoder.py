import requests

def get_coordinates(place):

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": place,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "smart-route-ai-project"
    }

    response = requests.get(url, params=params, headers=headers)

    data = response.json()

    if len(data) == 0:
        return None

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])

    return lat, lon