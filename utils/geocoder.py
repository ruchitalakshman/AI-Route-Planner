import requests

def get_coordinates(place):

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": place,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "smart-route-ai-project (your_email@example.com)"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)

        # check if request failed
        if response.status_code != 200:
            return None

        data = response.json()

        if not data:
            return None

        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])

        return lat, lon

    except Exception as e:
        return None