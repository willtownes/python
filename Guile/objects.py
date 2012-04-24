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
        self.armies = 0
    def assignplayer(self,player):
        '''assigns one of the players to the country. Player should be a "Player" object, not a name.'''
        self.player = player
        self.player.countries.add(self.name)
    def assignarmies(self,armies):
        armies = min([armies,self.player.spare_armies])
        self.player.spare_armies -= armies
        self.armies += armies
    def attack(self,dcountry,dice_a,invaders):
        '''The player on this country is attacking whichever player is on the defending country 'dcountry' (also a Country object).
        The dice_a argument specifies how many dice the attacker wants to roll.
        The invaders argument specifies how many armies the attacker will move into the new country if he/she wins the battle.
        Equivalent to a single round of attacking.'''
        if dcountry.name not in self.neighbors: #check to make sure dcountry borders the attacking country
            print("You can only attack bordering countries!")
            return #escape from the method, because attacking is not allowed
        #attacking country dice:
        if self.armies < 2:
            print("You don't have enough armies on this country to attack!")
            return #escape from the method, because attacking is not allowed
        elif self.armies < 3: dice_a = 1 #here it doesn't matter how many dice they want to roll. Only 1 is allowed.
        elif self.armies < 4: dice_a = min([dice_a,2]) #either 1 or 2 dice may be rolled.
        else:                 dice_a = min([dice_a,3]) #either 1, 2, or 3 dice may be rolled.
        #defending country dice:
        if dcountry.armies < 2: dice_d = 1
        else:                   dice_d = 2
        #simulating the rolls
        attackroll = sorted([Dice().roll() for i in range(dice_a)],reverse=True)
        defendroll = sorted([Dice().roll() for i in range(dice_d)],reverse=True)
        print("Attacker rolled: "+str(attackroll))
        print("Defender rolled: "+str(defendroll))
        d_losses = sum([i[0] > i[1] for i in zip(attackroll,defendroll)]) #compare attacker dice to defender dice
        a_losses = min([dice_a,dice_d]) - d_losses
        self.armies -= a_losses
        dcountry.armies -= d_losses
        #if the defender has no more armies on the territory, the attacker takes over.
        if dcountry.armies < 1:
            dcountry.player.countries.remove(dcountry.name) #the defending player no longer occupies the territory
            dcountry.player = self.player #the attacking player gains the territory
            self.player.countries.add(dcountry.name)
            invaders = min([self.armies-1,max([invaders,dice_a])]) #Ensure number of invaders to be within the acceptable range.
            dcountry.armies += invaders
            self.armies -= invaders
            
class Continent(object):
    def __init__(self,name,countries,points):
        self.name = name
        self.countries = countries
        self.points = points

class Player(object):
    def __init__(self,name):
        self.name = name
        self.spare_armies = 0
        self.countries = set([])
    def gainarmies(self,armies):
        self.spare_armies += armies
        
        
if __name__ == "__main__":
##    borders = getcountrydata('borders.csv')
##    countries = dict((i,Country(i,borders[i])) for i in borders) #dictionary of country objects with names as keys
##    ctlmap = getcontinentdata('continents.csv')
##    continents = dict((i,Continent(i,ctlmap[i],points[i])) for i in ctlmap)
##    players = ['William','Charlotte','Wes','Laura']
##    assert(len(players)) in range(2,7)
##    armies = 40 if len(players) == 2 else 40-5*(len(players)-2)
    #test data
    USA = Country('USA',['China'])
    China = Country('China',['USA'])
    Will = Player('Will')
    Ryan = Player('Adam')
    Will.gainarmies(5)
    Ryan.gainarmies(5)
    USA.assignplayer(Will)
    China.assignplayer(Ryan)
    USA.assignarmies(5)
    China.assignarmies(5)
