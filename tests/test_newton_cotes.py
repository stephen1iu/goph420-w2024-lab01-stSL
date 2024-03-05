from goph420_lab01.integration import integrate_newton

import unittest
import numpy as np

class TestNewtonCotes(unittest):
    
    def setUp(self):
        self.x=np.array([0,1,2,3,4,5,6,7])
        self.f=self.x+1
        self.intnew=integrate_newton(self.x,self.f,alg="trap")

    def test_trap_value(self):
        self.assertAlmostEqual(self.intnew, "value" , 1e-8)

    #testing simpson's 1/3 rule with odd npts
    def setUp(self):
        self.x=np.array([0,1,2,3,4,5,6])
        self.f=self.x**2+1
        self.intnew=integrate_newton(self.x, self.f, alg="simp")
    
    def test_trap_value(self):
        self.assertAlmostEqual(self.intnew, "value", 1e-8)

    #testing simpson's 1/3 and 3/8 rule with even npts
    def setUp(self):
        self.x=np.array([0,1,2,3,4,5,6,7])
        self.f=self.x**2+1
        self.intnew=integrate_newton(self.x, self.f, alg="simp")

    def test_trap_value(self):
        self.assertAlmostEqual(self.intnew, "value", 1e-8)