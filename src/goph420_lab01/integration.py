import numpy as np


def integrate_newton(x,f,alg="trap"):
    """
    Inputs
    ------
    x: x value of coordinates
    f: function value at x coordinates 
    alg: optional string (default="trap"), str of "simp"

    Returns
    -------
    float
    """
    x=np.array([x])
    f=np.array([f])
    N=len(x)
    area=0
    intervals=N//2
    sumx=np.array([[]])
    if alg=="trap":
        for i in range (0,N-1):
            area+=((x[i+1]-x[i])/2)*(f[i+1]+f[i])
        return area
    elif alg=="simp":
        if N>=3 and N % 2==0:
            for i in range (1,N-3,2):
                sumx[0]+=f[i]
            for i in range (2,N-4,2):
                sumx[1]+=f[i]
            area=1/3*intervals*(f[0]+4*sumx[0]+2*sumx[1]+f[N-1])+((x[N]-x[0])/8*(f[N-3]+3*f[N-2]+3*f[N-1]+f[N]))
        elif N>=3 and N % 2!=0:
            for i in range (1,N,2):
                sumx[0]+=f[i]
            for i in range (2,N-1,2):
                sumx[1]+=f[i]
            area=1/3*intervals*(f[0]+4*sumx[0]+2*sumx[1]+f[N-1])
            #np.array([[2*x[i]**2-3*x[i]+1, 4*x[i]-4*x[i]**2, 2*x[i]**2-x[i]]])
        return area
    else:
        raise ValueError ("Invalid algorithm entered, expected 'simp' or 'trap'")

def integrate_gauss(f, lims, npts):
    """
    Inputs
    ------
    f: callable
    lims: upper and lower bounds of integration 
    npts: optional (default=3), int of 1,2,3,4,5

    Returns
    -------
    float
    """

