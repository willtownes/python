#Agent Behavior Algorithm
#By Will Townes 10 Sept. 2009
import randspice
import random
rows = 5
columns = 5
agents = 15

#agent_stats lists agent ID, wealth (amt spice) and position.
#Each agent starts with 0-5 units of spice (random allocation)
agent_stats = []
spaces = range(0,rows*columns) #list all possible starting positions
for ID in range(1,agents+1): #avoid using 0 as an agent ID
    ispace = random.choice(spaces) #pick a random space
    agent_stats.append([ID,random.randint(0,5),ispace])
    spaces.remove(ispace)

#print summary of agent stats
header = ["agent ID","Wealth","position"]
disp_agent_stats = agent_stats[:]
disp_agent_stats.insert(0,header)
print disp_agent_stats


#initialize agentfield matrix on the spicefield
#if agency ID is zero, that means there is no agent in that cell.
#spicefield = randspice.randspice(rows,columns)
#agentfield = spicefield[:]
#for i in range(0,rows):
#    for j in range(0,columns):
#        agentposition[i][j] = 0 #zero out all values
        
#print "agent position matrix zeroed out", agentposition


    
    
            
    
    
    
