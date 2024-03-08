from goph420_lab01.integration import integrate_gauss

from scipy.integrate import fixed_quad
import unittest
import numpy as np


class TestGaussLegendre(unittest.TestCase):
    
    def setUp(self):
        self.lims=np.array([0,8])

    def test_npts1(self):
        #n=1
        def f(x):
            return x+1
        integrate_gauss(f, self.lims, 1)

    def test_npts2(self):
        #n=3
        def f(x):
            return x**3+2*x**2+x+1
    def test_npts3(self):
        #n=5
        def f(x):
            return 
    def test_npts4(self):
        #n=7
        def f(x):
            return 
    def test_npts5(self):
        #n=9
         def f(x):
            return 

if __name__=="__main__":
    unittest.main()