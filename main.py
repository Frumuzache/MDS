import urllib.request
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=44.4268&longitude=26.1025&current=temperature_2m"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

temperature = data["current"]["temperature_2m"]
print(f"Current temperature in Bucharest: {temperature}°C")
