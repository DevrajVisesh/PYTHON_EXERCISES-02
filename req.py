import requests

city = input("Enter City Name:")
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'b20531abd8dae982352ae25e8340f985')
d = r.json()
print("Tempurature for city",city,"is",d["main"]["temp"])