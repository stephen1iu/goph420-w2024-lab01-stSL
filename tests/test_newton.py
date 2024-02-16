# from goph420_lab01.integration import (
#     integrate_newton,
# )
import numpy as np

x=np.array([1,2,3,4,5,6,7])
f=np.array([2,3,4,5,6,7,8])
sumx=np.array([0,0])
N=4
intervals=N//2

if N>=3 and N % 2==0:
    print ("1")
elif N>=3 and N % 2!=0:
    print ("2")

# integrate_newton(x,f,alg="trap")