import requests

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjNiOTg1OTczNGUyYzQwNDc5YTgwMGI1ZmNlMzI0N2YyIiwiaCI6Im11cm11cjY0In0="

def get_routes(start, end):

    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [
            [start[1], start[0]],
            [end[1], end[0]]
        ],
        "alternative_routes": {
            "target_count": 3
        }
    }

    try:
        response = requests.post(url, json=body, headers=headers)

        if response.status_code != 200:
            print("API ERROR:", response.text)
            return []

        data = response.json()

        if "routes" not in data:
            print("Unexpected API response:", data)
            return []

        return data["routes"]

    except Exception as e:
        print("Route API failed:", e)
        return []