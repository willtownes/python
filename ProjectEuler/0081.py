'''
Project Euler Problem 81
Find the minimal path sum across the provided matrix
'''
import numpy as np

def parsematrix(filename='matrix.txt'):
    '''reads in the matrix data from file'''
    with open(filename) as ifile:
        matrix=ifile.readlines()
    matrix=[i.strip('\n').split(',') for i in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j]) #convert everything to integer type
    matrix=np.matrix(matrix)
    return matrix

def getsum(matrix,psum=0):
    '''recursive function that returns the minimum path sum through a numeric matrix. Does not identify the path followed'''
    psum+=matrix[0,0]
    if matrix.size==1: #reached final cell
        pass
    else:
        m_right=matrix[:,1:] #slice off first column if path goes to the right
        m_down=matrix[1:,:] #slice off first row if path goes down
        if 0 in m_down.shape: #bottom edge reached. Must move to the right only
            sum_right=getsum(m_right)
            psum+=sum_right
        elif 0 in m_right.shape: #right edge reached. Must move down only
            sum_down=getsum(m_down)
            psum+=sum_down
        else: #somewhere in the middle of the matrix
            sum_right=getsum(m_right)
            sum_down=getsum(m_down)
            if sum_right < sum_down: psum+=sum_right
            else: psum+=sum_down
    return psum

if __name__=="__main__":
    #testmat=np.matrix('131,673,234,103,18,201,96,342,965,150,630,803,746,422,111,537,699,497,121,956,805,732,524,37,331')
    #testmat.resize(5,5)
    testmat=parsematrix()
    assert testmat.shape==(80,80)
    res=getsum(testmat)
    print(res)