from goph420_lab01.integration import integrate_newton

import unittest
import numpy as np

#function of y=x+1
x=np.array([1,2,3,4,5,6,7])
f=np.array([2,3,4,5,6,7,8])

integrate_newton(x,f)
print(integrate_newton)