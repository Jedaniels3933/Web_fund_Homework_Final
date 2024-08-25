import requests 
import json
from bs4 import BeautifulSoup

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/bodies"
    response = requests.get(url)
    planets = response.json()['bodies']

    f_planets = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'Unknown')
            mass = planet.get('massValue', 'Unknown')
            orbit_period = planet.get('sideralOrbit', 'Unknown')
            f_planets.append(f"Name: {name}, Mass: {mass}, Orbit Period: {orbit_period}")
    return f_planets

def heaviest_planet():
    url = "https://api.le-systeme-solaire.net/rest/bodies/bodies"
    response = requests.get(url)
    planets = response.json()['bodies']

    max_mass = 0
    heaviest_planet = ''
    for planet in planets:
        if planet['isPlanet']:
            mass = planet.get('massValue', 'Unknown')
            if mass != 'Unknown':
                mass = float(mass)
                if mass > max_mass:
                    max_mass = mass
                    heaviest_planet = planet.get('englishName', 'Unknown')
    return heaviest_planet

planets = fetch_planet_data()
planet_name, mass = heaviest_planet(planets)

print(f"{planet_name} is the heaviest planet, it's mass is  {mass} kg.")



fetch_planet_data()

















response = requests.get