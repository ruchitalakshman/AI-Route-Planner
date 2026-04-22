import requests

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjNiOTg1OTczNGUyYzQwNDc5YTgwMGI1ZmNlMzI0N2YyIiwiaCI6Im11cm11cjY0In0="

url = "https://api.openrouteservice.org/v2/directions/driving-car"

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

body = {
    "coordinates": [
        [77.5946,12.9716],
        [77.6146,12.9352]
    ]
}

response = requests.post(url, json=body, headers=headers)

print(response.status_code)
print(response.text)