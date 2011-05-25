#Spiceland
#Trying to create a cellular automaton, by Will Townes

width = 5
height = 5

class Cell:
    def initial(self):
        self.spicecount = 0
        self.agentpresent = 0
        self.positionx = 0
        self.positiony = 0
        
    def growspice(self):
        if self.agentpresent == 0:
            self.spicecount = self.spicecount + 1
        else:
            self.spicecount = self.spicecount - 1

    def moveagent(self):
        if self.agentpresent == 0:
            self.agentpresent = AGENT_ID
            
        

class Matrix:
    def size(self,width,height):
        self.width = width
        self.height = height
        
                
                
        
