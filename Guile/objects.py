'''This module defines classes for the dice, each country, and each player.'''

import random,csv,pickle
points = {
    'Oceania':2,
    'Asia':7,
    'Africa':3,
    'Europe':5,
    'North America':5,
    'South America':2}

def getcountrydata(csvfile):
    '''reads in the csv file containing the country border info, returns a list of dictionaries'''
    info = [row for row in csv.DictReader(open(csvfile,'rb'))]
    countries = {}
    for i in info:
        name = i['']
        neighbors = [country for country in i if i[country] == '1']
        assert name not in neighbors #a country cannot border itself!
        countries[name] = neighbors #append to collector dictionary
    return countries

def getcontinentdata(csvfile):
    '''reads in the csv file containing the country:continent mapping and returns list of dictionaries'''
    info = [row for row in csv.reader(open(csvfile,'rb'))][1:] #skipping header row and initializing country lists for each continent
    continents = dict((i[1],[]) for i in info) 
    for i in info:
        continents[i[1]].append(i[0])
    return continents

class Dice(object):
    '''the dice object is used to simulate rolling a dice.'''
    def roll(self):
        return random.randint(1,6)

class Battle(object):
    def __init__(self,attacker,defender):
        self.attacker = attacker
        self.defender = defender

class Country(object):
    def __init__(self,name,neighbors):
        self.name = name
        self.neighbors = neighbors
    def assignplayer(self,player):
        '''assigns one of the players to the country.'''
        self.player = player

class Continent(object):
    def __init__(self,name,countries,points):
        self.name = name
        self.countries = countries
        self.points = points

class Player(object):
    def __init__(self,name):
        self.name = name
        self.armies = 0
        self.countries = []
    def assignarmies(self,armies):
        self.armies += armies
        
if __name__ == "__main__":
    borders = getcountrydata('borders.csv')
    countries = dict((i,Country(i,borders[i])) for i in borders) #dictionary of country objects with names as keys
    ctlmap = getcontinentdata('continents.csv')
    continents = dict((i,Continent(i,ctlmap[i],points[i])) for i in ctlmap)
    players = ['William','Charlotte','Wes','Laura']
    assert(len(players)) in range(2,7)
    armies = 40 if len(players) == 2 else 40-5*(len(players)-2)
