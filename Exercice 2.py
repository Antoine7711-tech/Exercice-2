import requests 

#exercice 2.a

hp_Harry_potter = requests.get('https://www.themoviedb.org/movie/671-harry-potter-and-the-philosopher-s-stone')
print(hp_Harry_potter.status_code)

Lord_of_the_rings = requests.get('https://www.themoviedb.org/movie/120-the-lord-of-the-rings-the-fellowship-of-the-ring')
print(Lord_of_the_rings.status_code)


print("---------------------------------")
#exercice 2.b
import requests
from datetime import date, timedelta

# --- Coordonnées de la FUCaM ---
latitude = 50.4489
longitude = 3.9523

# --- On calcule la date de demain ---
tomorrow = date.today() + timedelta(days=1)

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m", #Température à 2m du sol
    "timezone": "Europe/Brussels",
    "start_date": tomorrow.strftime("%Y-%m-%d"),
    "end_date": tomorrow.strftime("%Y-%m-%d")
}

response = requests.get(url, params=params)

print("Status:", response.status_code)

data = response.json() #convertie la réponse de l'API qui est en JSON en dictionnaire Python

# --- Récupération de la température horaire ---
hours = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]

print(f"Météo à la FUCaM pour le {tomorrow} :") #fstring
#Tomorrow est un objet date, il sera affiché au format AAAA-MM-JJ
for t, temp in zip(hours, temps): #Zip est une paire de la liste de chaîne hours et temps.
    print(f"{t} → {temp}°C")

#exercice 2.c
print("---------------------------------")

from bs4 import BeautifulSoup

headers = {
    "Accept-Language": "en-US,en;q=0.9"
}

hp_Harry_potter_2 = requests.get('https://www.themoviedb.org/movie/671-harry-potter-and-the-philosopher-s-stone', headers=headers)
Lord_of_the_rings_2 = requests.get('https://www.themoviedb.org/movie/120-the-lord-of-the-rings-the-fellowship-of-the-ring', headers=headers)

#parser car html vers xml
soup_hp = BeautifulSoup(hp_Harry_potter_2.text, 'html.parser')
soup_LOTR = BeautifulSoup(Lord_of_the_rings_2.text, 'html.parser')

# Exemple de récupération du synopsis (le sélecteur peut varier selon le site)
synopsis_tag_1 = soup_hp.find("div", class_="overview")
print("Synopsis of Harry Potter and the Philosopher's Stone:")
print("")
print(synopsis_tag_1.get_text(strip=True))
synopsis_tag_2 = soup_LOTR.find("div", class_="overview")
print("")
print("Synopsis of The Lord of the Rings: The Fellowship of the Ring:")
print("")
print(synopsis_tag_2.get_text(strip=True))