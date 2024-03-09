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
    alg=alg.strip().lower()
    x=np.array(x)
    f=np.array(f)
    if len(x)!=len(f):
        raise ValueError (f"dimensions of x, {len(x)} and f, {len(x)} not compatible")
    N=len(x)
    if len(x.shape)==2 or len(f.shape)==2:
        raise ValueError ("array must be 1D, x or f is a 2D array")
    integral=0
    if alg=="trap":
        for i in range (0,N-1):
            integral+=((x[i+1]-x[i])/2)*(f[i+1]+f[i])
        return integral
    
    elif alg=="simp":
        #even case
        if N>=3 and N % 2==0:
            for i in range (0,N-4,2):
                integral+=((x[i+2]-x[i])/6)*(f[i]+4*f[i+1]+f[i+2])
            integral+=((x[N-1]-x[N-4])/8)*(f[N-4]+3*f[N-3]+3*f[N-2]+f[N-1])
            
        #odd case
        elif N>=3 and N % 2!=0:
            for i in range (0,N-2,2):
                integral+=((x[i+2]-x[i])/6)*(f[i]+4*f[i+1]+f[i+2])
        return integral
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
    if len(lims)!=2:
        raise ValueError (f"dimensions of limit array is {len(lims)}, expected: 2")
    a=lims[0]
    b=lims[1]
    npts=int(npts)
    integral=0

    n=2*npts-1

    if npts==1:
        points=[0.0]
        weights=[2.0]

    elif npts==2:
        points=[-1/np.sqrt(3), 1/np.sqrt(3)]
        weights=[1.0, 1.0]

    elif npts==3:
        points=[-np.sqrt(3/5), 0, np.sqrt(3/5)]
        weights=[5/9, 8/9, 5/9]

    elif npts==4:
        points=[-np.sqrt((3/7)+2/7*np.sqrt(6/5)), -np.sqrt((3/7)-2/7*np.sqrt(6/5)),
                np.sqrt((3/7)-2/7*np.sqrt(6/5)), np.sqrt((3/7)+2/7*np.sqrt(6/5))]
        weights=[(18-np.sqrt(30))/36, (18+np.sqrt(30))/36, (18+np.sqrt(30))/36, (18-np.sqrt(30))/36]

    elif npts==5:
        points=[-1/3*(np.sqrt(5+2*np.sqrt(10/7))), -1/3*(np.sqrt(5-2*np.sqrt(10/7))), 0,
                1/3*(np.sqrt(5-2*np.sqrt(10/7))), 1/3*(np.sqrt(5+2*np.sqrt(10/7)))]
        weights=[(322-13*np.sqrt(70))/900, (322+13*np.sqrt(70))/900, 128/225,
                (322+13*np.sqrt(70))/900, (322-13*np.sqrt(70))/900]
    else:
        raise ValueError ("invalid value of npts, expected 1, 2, 3, 4, 5")
    
    transpoints=np.zeros(npts)
    transweights=np.zeros(npts)

    for i in range (0, npts):
        transpoints[i]=((a+b)+(b-a)*points[i])/2.0
        transweights[i]=((b-a)/2)*weights[i]
    for i in range (0,npts):
        integral+=transweights[i]*f(transpoints[i])
    return integral