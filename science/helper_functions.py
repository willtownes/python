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

def distmat(x,row=True,squared=False):
    """Returns the matrix of all pairwise distances between the rows of x.
    If row=False, returns matrix of pairwise distances between column vectors."""
    if row==False: xxt = np.inner(x,x)
    elif row==True: xxt = np.outer(x,x)
    else: raise TypeError("row must be True/False")
    n = xxt.shape[0]
    dmat = np.zeros((n,n))
    for i in xrange(n):
        xxt_ii = xxt[i][i]
        for j in xrange(i+1,n):
            d = xxt_ii + xxt[j][j] - 2*xxt[i][j]
            dmat[i][j] = d
            dmat[j][i] = d
    if squared: return dmat
    else: return np.sqrt(dmat)

def phi_basis(sq_distance_matrix,rho):
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
    x= np.array([-1.87,-1.76,-1.67,-1.22,-0.07,0.11,0.67,1.60,2.22,2.51])
    Phi = phi_basis(distmat(x,squared=True),rho=1)
    Phi_sqt = matrix_sqt(Phi)
    print(np.max(np.abs(Phi-Phi_sqt.dot(Phi_sqt.T))))
    #plt.plot(x,Phi);