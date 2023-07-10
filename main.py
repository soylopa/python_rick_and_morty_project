import random
from itertools import chain, repeat
import requests
def characterSelection():
    character_number = random.randint(1,160)
    url = 'https://rickandmortyapi.com/api/character/{}'.format(character_number)
    response = requests.get(url)
    character = response.json()

    return {
        'id': character['id'],
        'name': character['name'],
        'species': character['species']
    }
characterSelection()

def locationSelection():
    location_number = random.randint(1,160)
    locations = 'https://rickandmortyapi.com/api/location/{}'.format(location_number)
    response = requests.get(locations)
    location = response.json()

    return {
        'id': location['id'],
        'name': location['name'],
        'type': location['type'],
        'dimension': location['dimension']
    }
locationSelection()

def scapePortal():
    planet_number = random.randint(1,60)
    locations = 'https://rickandmortyapi.com/api/location/{}'.format(planet_number)
    response = requests.get(locations)
    location = response.json()

    return {
        'id': location['id'],
        'name': location['name'],
        'dimension': location['dimension']
    }
scapePortal()

def letsPlayMmmmorty():
    my_character = characterSelection()
    print('Oh, I-i think I am d-d-drunk, I me-mean, I am {}'.format(my_character['name']))
    my_locations = locationSelection()
    our_scape_route_1 = scapePortal()
    our_scape_route_2 = scapePortal()
    our_scape_route_3 = scapePortal()
    print('It looks like we are trap in {}.'.format(my_locations['name']))
    route = input("We must go to somewhere else: choose! {}, {}, {}.".format(our_scape_route_1['name'], our_scape_route_2['name'], our_scape_route_3['name']))
    is_route_1 = route == our_scape_route_1['name']
    is_route_2 = route == our_scape_route_2['name']
    is_route_3 = route == our_scape_route_3['name']
    lets_scape = input("What is your plan? ")
    lets_die = is_route_3

    if lets_scape == is_route_1 or is_route_2:
        print('Lets go')

    elif lets_die == is_route_3:
        print('Idiot, we will die') 
        
    else:
        print('Choose something!')
        
letsPlayMmmmorty()