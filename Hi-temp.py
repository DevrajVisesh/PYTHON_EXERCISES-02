import requests
x = {}
y = []
for i in range(5):
    city = input("Enter City Name:")
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'b20531abd8dae982352ae25e8340f985')
    d = r.json()
    x[i] = d
    y.append(x[i]['main']['temp'])
print(y)
a = max(y)
print(a)
for i in range(5):
    if a == x[i]['main']['temp']:
       print("Highest tempurature",city,"is",d["main"]["temp"])