from goph420_lab01.integration import integrate_newton

import unittest
import numpy as np

class TestNewtonCotes(unittest.TestCase):

    def test_trap_value(self):
        self.x=np.array([0,1,2,3,4,5,6,7])
        self.f=self.x+1
        self.intnew=integrate_newton(self.x,self.f,alg="trap")
        self.assertEqual(self.intnew, 31.5)

    #testing simpson's 1/3 rule with odd npts    
    def test_simp_odd_value(self):
        self.x=np.array([0,1,2,3,4,5,6])
        self.f=self.x**2+1
        self.intnew=integrate_newton(self.x, self.f, alg="simp")
        self.assertAlmostEqual(self.intnew, 78, 5)

    #testing simpson's 1/3 and 3/8 rule with even npts
    def test_simp_even_value(self):
        self.x=np.array([0,1,2,3,4,5,6,7])
        self.f=self.x**2+1
        self.intnew=integrate_newton(self.x, self.f, alg="simp")
        self.assertAlmostEqual(self.intnew, 364/3, 5)

if __name__=="__main__":
    unittest.main()