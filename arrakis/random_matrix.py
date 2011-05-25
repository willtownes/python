#Sets up a matrix of arbitrary dimensions with random integer values
#between 0 and 9, and prints out the matrix
#By Will Townes, 08/2010

#probably can simplify this part and combine it with the "create_matrix" function.
def random_matrix(height,width):    
    import random
    A = []
    for i in range(height):
        A.append([])
    for i in range(height):
        for j in range(width):
            A[i].append([])
    
    for i in range(height):
        for j in range(width):
            A[i][j] = random.randint(0,9)
    #for i in range(height):
    #    print A[i]
    return A;

#Create the basic properties of a given cell in the matrix:
class cell(object):
    row = None
    col = None
    spice = None
    has_agent= False
    
    def __init__(self, row=None, col=None, spice=None, has_agent= False):
        if row is not None:
            self.row = row
        if col is not None:
            self.col = col
        if spice is not None:
            self.spice = spice
        if has_agent is not False:
            self.has_agent = has_agent
            
#Generates a matrix of arbitrary size where each cell is an object as defined above.  
def create_matrix(rows,cols):
    C = random_matrix(rows,cols)
    D = C[:]
    for i in range(rows):
        for j in range(cols):
            C[i][j]= cell(i,j,D[i][j])
            #only need these print commands for debugging
            print C[i][j].row
            print C[i][j].col
            print C[i][j].spice
    return C

#Create the basic properties of an agent:
class agent(object):
    row = None
    col = None
    spice = None
    
    def __init__(self, row=None, col=None, spice=None):
        if row is not None:
            self.row = row
        if col is not None:
            self.col = col
        if spice is not None:
            self.spice = spice

#function to generate an arbitrary number of agents
def create_agents(number):
    if number < 0:
        print 'error- number must be positive'
    else:
        B = range(number)
        for i in B:
            B[i] = agent()
    return B


    


