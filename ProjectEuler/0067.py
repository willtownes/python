data0 = open('triangle.txt','r').readlines()
def parsedata(data0):
    data0 = [i.split(' ') for i in data0]
    data0 = [[int(i) for i in j] for j in data0]
    return data0
data = parsedata(data0)[:]
def findmaxpath(data):
    '''find maximum sum of all paths from top to bottom of the triangular arrray.'''
    #Aggregates the sum of lower rows into the cells above.
    start = len(data)-2
    for i in range(start,-1,-1):
        for j in range(len(data[i])):
            data[i][j]+= max(data[i+1][j],data[i+1][j+1])
    return data[0][0]
print("Answer is:  "+str(findmaxpath(data)))
