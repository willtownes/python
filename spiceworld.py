import numpy, numpy.random, random
from operator import itemgetter
rows = 10
cols = 10
agent_count = 50

class Agent:
    def __init__(self,ID):
        self.ID = ID
        self.savings = 0
        self.metabolism = 1
        self.status = 'unborn'
        self.neighborcells = []
    def birth(self,row,col):
        self.status = 'alive'
        self.row = row
        self.col = col
    def eat(self):
        self.savings -= 1
    def move(self,row,col):
        self.row = row
        self.col = col

class Cell:
    def __init__(self,row,col,spice):
        self.ID = (row,col)
        self.spice = spice
        self.neighborcells = []
        self.hasagent = 0
        
spicefield = numpy.random.random_integers(0,10,(rows,cols))
agentfield = numpy.zeros((rows,cols),dtype=int)

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

#agents look around and rank choices of best nearby cells. Current cell counts as a "neighbor" too!
for k in agents.keys(): #do this for all agents
    for i in range(agents[k].row-1,agents[k].row+2): #neighboring rows
        for j in range(agents[k].col-1,agents[k].col+2): #neighboring cols
            if i >= 0 and j >= 0: #exclude negative indices (edges/corners)
                try:
                    agents[k].neighborcells.append((i,j,spicefield[i,j]))
                except:
                    pass #don't append to neighborcells list when out of range (edge/corners).
            agents[k].neighborcells.sort(key = itemgetter(2),reverse = True) #rank descending by spice count

print 'spicefield\n',spicefield,'\n'
print 'agent positions\n',agentfield

import matplotlib.pyplot as plt
plt.matshow(spicefield)
plt.matshow(agentfield)
plt.show()
#Now we define the rules for spice regrowing, agent savings, agent movement decision
#Assume spice regrows one unit per iteration. Agent can harvest two units per iteration.
#Agent must consume one unit to survive each iteration with no movement.
#If agent moves it must use up one unit in the move (2 per iteration).
#If agent can harvest two units it will put one "in savings"
#Agent always tries to move to neighboring cell with maximum spice
#Order of which agent gets to decide when to move is randomized at each iteration
#If spice is zero or one agent only harvests what is there (no savings).
#Agent can survive on zero spice cells by using up savings.
        
    
