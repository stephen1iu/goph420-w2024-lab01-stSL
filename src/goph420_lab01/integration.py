import numpy as np


def integrate_newton(x,f,alg="trap"):
    """
    Inputs
    ------
    x: x value of coordinates
    f: function value of x coordinates 
    alg: optional string (default="trap"), str of "simp"

    Returns
    -------
    float
    """
    N=len(x)
    area=0
    intervals=N//2
    sumx=np.ndarray([[]])
    if alg=="trap":
        for i in range (0,N):
            area+=((x[i+1]-x[i])/2)*(f[i+1]+f[i])
    elif alg=="simp":
        if N>=3 and N//2==0:
            pass
        elif N>=3 and N//2!=0:
            for i in range (1,N,2):
                sumx[0]+=f[i]
            for i in range (2,N-1,2):
                sumx[1]+=f[i]
            area=1/3*intervals*(f[0]+4*sumx[1]+2*sumx[2]+f[N])
            #np.ndarray([[2*x[i]**2-3*x[i]+1, 4*x[i]-4*x[i]**2, 2*x[i]**2-x[i]]])


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

    