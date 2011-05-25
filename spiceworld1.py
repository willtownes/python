import numpy, numpy.random, random
from operator import itemgetter
#initial parameters:
rows = 10
cols = 10
agent_count = 50
timer = 0
spicefield = numpy.random.random_integers(0,10,(rows,cols))
agentfield = numpy.zeros((rows,cols),dtype=int)

class Agent:
    def __init__(self,ID):
        self.ID = ID
        self.savings = 0
        self.harvest_rate = 2
        self.metabolism = 1
        self.status = 'unborn'
        self.neighborcells = []
        self.age = 0
    def birth(self,row,col):
        self.status = 'alive'
        self.row = row
        self.col = col
    def harvest(self,spicefield):
        if self.harvest_rate <= spicefield[self.row,self.col]:
            self.savings += self.harvest_rate
        else:
            self.savings += spicefield[self.row,self.col]
    def move(self,row,col):
        #incorporate eating into this method too since it depends on whether they move or not.
        self.row = row
        self.col = col
    def rankneighbors(self,spicefield):
        self.neighborcells = [] #reset list of neighboring cells.
        rows = spicefield.shape[0]
        cols = spicefield.shape[1]
        for i in range(self.row-1,self.row+2): #neighboring rows
            for j in range(self.col-1,self.col+2): #neighboring cols
                if i >= 0 and j >= 0 and i < rows and j < cols: #exclude out-of-range indices(edges/corners)
                    self.neighborcells.append((i,j,spicefield[i,j])) #i,j are location, 3rd element is amt of spice.
                self.neighborcells.sort(key = itemgetter(2),reverse = True) #rank descending by spice count

#scenarios for agent movement:
#1. top choice cell has no other interested agents. Agent goes to that cell and burns normal energy
#2. Agent must compete with others for currently empty cell (all have it as top choice). Cell goes to a random agent.Others try for second choice.
#3. Agent must compete with others for currently occupied cell. Agents bid to trade places with occupant.Max bid is total savings minus metabolism needed to move
#   Occupant will only agree to move if the bid + spice in new cell exceeds spice in current cell.

#The following occur to complete a full cycle:
#0. [DONE]Cells grow spice by "growthrate" amount. 
#1. [DONE]Agents harvest spice in current cell at the given rate "harvestrate", add that to their savings.
#2. [DONE]Agents rank nearby cells to decide where they want to move.
#3. Agents move to optimal nearby cell (or choose to stay in place).
#4. As each agent moves, its age increase by one, and it burns 2x metabolism from savings for movement (1x to stay in place).
#5. Once all agents have had a chance to move, the timer is updated by +1 and the cycle starts again.
    #def bid(self,cell):

class Cell:
    def __init__(self,row,col,spice):
        self.ID = (row,col)
        self.row = row
        self.col = col
        self.spice = spice
        self.growthrate = 1
        self.neighboragents = []
        self.hasagent = 0
        self.age = 0
    def growspice(self):
        self.spice += self.growthrate
    #def auction(self,agentfield):
    #    self.neighboragents = []
    #    rows = agentfield.shape[0]
    #    cols = agentfield.shape[1]
    #    for i in range(self.row-1,self.row+2): #neighboring rows
    #        for j in range(self.col-1,self.col+2): #neighboring cols
    #            if i >= 0 and j >= 0 and i < rows and j < cols:

while agent_count > len(spicefield[spicefield.nonzero()]): #cannot have more agents than cells with spice.
    agent_count = input('Too many agents, enter a smaller number   ')

agents = dict((i,Agent(i)) for i in range(1,agent_count+1)) #dictionary storing all the agent objects

cells = {}  #dictionary storing cell objects
freecells = [] #list of cells with no agents and spice > 0.
for i in range(rows):
    for j in range(cols):
        cells[(i,j)] = Cell(i,j,spicefield[i,j]) #create cell object with ID (i,j)
        if cells[(i,j)].spice > 0:
            freecells.append((i,j)) #add cell ID to list of freecells if it has spice.

#birth of agent is assigning it to an empty cell where spice is at least one for iteration 0.
for i in agents.keys():
    while agents[i].status == 'unborn':
        [row_try,col_try] = random.choice(freecells) #pick random cell index from dictionary
        agents[i].birth(row_try,col_try)
        agentfield[row_try,col_try] = agents[i].ID #update agentfield matrix
        cells[(row_try,col_try)].hasagent = agents[i].ID #update cell object
        freecells.remove((row_try,col_try)) #update free cells list because this cell is now occupied.

#cells grow spice, update spicefield
def growspice(cells,spicefield):
    for i in cells.keys():
        cells[i].growspice()
        spicefield[cells[i].row,cells[i].col] += cells[i].growthrate
        if spicefield[cells[i].row,cells[i].col] != cells[i].spice: #debugging only.
            input('ERROR- spicefield and cell object not synchronized!') #debugging only
    return cells,spicefield

#agents harvest spice on their current cell
def harvestspice(agents,cells,spicefield):
    for i in agents.keys():
        agents[i].harvest(spicefield)
        cells[(agents[i].row,agents[i].col)].spice -= agents[i].harvest_rate
        spicefield[agents[i].row,agents[i].col] -= agents[i].harvest_rate
    return agents,cells,spicefield

#agents look around and rank choices of best nearby cells. Current cell counts as a "neighbor" too!
def rankneighbors(agents,spicefield):
    for i in agents.keys(): #do this for all agents
        agents[i].rankneighbors(spicefield)
    return agents,spicefield

(cells,spicefield) = growspice(cells,spicefield)
(agents,cells,spicefield) = harvestspice(agents,cells,spicefield)
(agents,spicefield) = rankneighbors(agents,spicefield)

print 'spicefield\n',spicefield,'\n'
print 'agent positions\n',agentfield

import matplotlib.pyplot as plt
plt.matshow(spicefield)
plt.matshow(agentfield)
plt.show()
        
    
