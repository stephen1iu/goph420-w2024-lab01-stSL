from goph420_lab01.integration import (
    integrate_newton,
)
import numpy as np

x=np.ndarray([[1,2,3,4]])
f=np.ndarray([[2,3,4,5]])

integrate_newton(x,f,alg="trap")