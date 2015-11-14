"""Miscellaneous functions and code patterns that are useful in scientific computing"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln

def pdf_factory(d):
    """Returns Chi-Distribution PDFs indexed by parameter d"""
    def pdf_z(z,logscale=False):
        """Compute PDF of Chi-Distribution with parameter %d evaluated at z"""%d
        val = (1-d/2.0)*np.log(2.0) - gammaln(d/2.0) + (d-1)*np.log(z) - z**2/2.0
        if logscale:
            return val
        else:
            return np.exp(val)
    return pdf_z

def dist(a,b):
    """calculate euclidean distance between two points a and b"""
    return np.linalg.norm(a-b)

def distmat(A,B,row=True,squared=False):
    """Returns the matrix of all pairwise distances between the rows of A and rows of B.
    If row=False, returns matrix of pairwise distances between column vectors.
    Does not accept vectors! Convert to arrays or matrices first!"""
    #to-do: can speed up special case of distmat(A,A) by taking advantage of symmetry
    if row==False:
        A = A.T
        B = B.T
    assert(A.shape[1]==B.shape[1])
    AAt = A.dot(A.T)
    BBt = B.dot(B.T)
    ABt = A.dot(B.T)
    n,m = ABt.shape
    dmat = np.zeros((n,m))
    for i in xrange(n):
        for j in xrange(m):
            dmat[i][j] = AAt[i,i] + BBt[j,j] - 2*ABt[i,j]
    if squared: return dmat
    else: return np.sqrt(dmat)

def phi_basis(sq_distance_matrix,rho=1):
    """Given a matrix of squared pairwise distances,
    computes the radial basis functions of each point,
    with the scale/bandwidth parameter rho. phi(t) = exp(-t/rho)"""
    return np.exp((-1./rho)*sq_distance_matrix)

def matrix_sqt(mat):
    """given some positive-definite matrix A, computes its square root matrix B,
    using the spectral decomposition, such that A = BB^T."""
    vals,vects = np.linalg.eigh(mat)
    return vects.dot(np.diag(np.sqrt(vals)))

if __name__=="__main__":
    #x= np.array([-1.87,-1.76,-1.67,-1.22,-0.07,0.11,0.67,1.60,2.22,2.51])
    #Phi = phi_basis(distmat(x,squared=True),rho=1)
    #Phi_sqt = matrix_sqt(Phi)
    #print(np.max(np.abs(Phi-Phi_sqt.dot(Phi_sqt.T))))
    #plt.plot(x,Phi);