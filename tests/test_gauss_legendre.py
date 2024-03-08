from goph420_lab01.integration import integrate_gauss

from scipy.integrate import fixed_quad
import unittest
import numpy as np


class TestGaussLegendre(unittest.TestCase):
    
    def setUp(self):
        self.lims=np.array([0,8])

    def test_npts1(self):
        #x+1
        def f(x):
            return x+1
        self.integral=integrate_gauss(f, self.lims, 1)
        self.assertEqual(self.integral, 40)

    def test_npts2(self):
        #x^3 + 2x^2 + x + 1
        def f(x):
            return x**3+2*x**2+x+1
        self.integral=integrate_gauss(f, self.lims, 2)
        self.assertEqual(self.integral, 4216/3)

    def test_npts3(self):
        #x^5 + 3x^4 + 2x^3 + x^2 + 2x + 1
        def f(x):
            return x**5+3*x**4+2*x**3+x**2+2*x+1
        self.integral=integrate_gauss(f, self.lims, 3)
        self.assertEqual(self.integral, 984632/15)
    
    def test_npts4(self):
        #3x^7 + x^6 - x^5 + x^4 +x^3 -2x^2 + x
        def f(x):
            return 3*x**7+x**6-x**5+x**4+x**3-2*x**2+x
        self.integral=integrate_gauss(f, self.lims, 4)
        self.assertAlmostEqual(self.integral, 229411936/35, 7)

    def test_npts5(self):
        #n=9
        def f(x):
            return x**8+7*x**7+x**6+x**5+x**4+x**3+x**2-x-3
        self.integral=integrate_gauss(f, self.lims, 5)
        self.assertAlmostEqual(self.integral, 9432398104/315, 7)

if __name__=="__main__":
    unittest.main()