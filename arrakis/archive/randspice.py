#By Will Townes 10 Sept. 2009
#this will create a matrix with random integer values between 1 and 5
#Each cell of the matrix represents a location, values represent amt of spice
def randspice(rows,columns):
    import random
    irow = []
    randspice = []

#creates spice field of dimensions (rows,columns) full of zeros
    for j in range(0,columns):
        irow.append(0)
    for i in range(0,rows):
        randspice.append(irow[:])

#randomly populates each cell in spice field with between 0 and 5 units of spice.
    for i in range(0,rows):
        for j in range(0,columns):
            randspice[i][j] = random.randint(0,5)

    return randspice


#NEW FUNCTION
#this function will display the matrix in a more gridlike fashion.
#18 May 2010

def printmatrix(matrix):
    for row in matrix:
        print(row)

#NEW FUNCTION
#this function will compare the cell I'm in and find the location of the max spice value in adjacent cells
def findmax(matrix,row,column):
    location = [row,column]
    maxloc = [a,b]
    for i in range(row-1,row+1):
        for j in range(column-1,column+1):
            maxloc[1] = j
            elif j < 0 or j > len(matrix[0]):
                continue
            
        if i<0 or i > len(matrix):
            continue
            
