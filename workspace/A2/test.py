import os
import unittest
import numpy as np
from A2Part1 import genSine
from A2Part2 import genComplexSine
from A2Part3 import DFT
from A2Part4 import IDFT
from A2Part5 import genMagSpec

class TestAssignment(unittest.TestCase):

    def test_genSine(self):
        expected = np.array([ 0.54030231, -0.63332387, -0.93171798,  0.05749049,  0.96724906])
        actual = genSine(1.0, 10.0, 1.0, 50.0, 0.1)
        self.assertTrue(np.isclose(expected, actual).all())

    def test_genComplexSine(self):
        expected = np.array([ 1.0 + 0.j,  0.30901699 - 0.95105652j, -0.80901699 - 0.58778525j, -0.80901699 + 0.58778525j, 0.30901699 + 0.95105652j])
        actual = genComplexSine(1, 5)
        print 'expected:', np.imag(expected)
        print 'actual:', np.imag(actual)
        print np.isclose(np.imag(expected), np.imag(actual))
        self.assertTrue(np.allclose(np.real(expected), np.real(actual)))
        self.assertTrue(np.allclose(np.imag(expected), np.imag(actual)))

    def test_DFT(self):
        expected = np.array([10.0 + 0.0j,  -2. +2.0j,  -2.0 - 9.79717439e-16j, -2.0 - 2.0j])
        actual = DFT(np.array([1, 2, 3, 4]))
        self.assertTrue(np.isclose(expected, actual).all())

    def test_IDFT(self):
        expected = np.array([  1.00000000e+00 +0.00000000e+00j,   -4.59242550e-17 +5.55111512e-17j, 0.00000000e+00 +6.12323400e-17j,   8.22616137e-17 +8.32667268e-17j])
        actual = IDFT(np.array([1, 1, 1, 1]));
        self.assertTrue(np.isclose(expected, actual).all())

    def test_genMagSpec(self):
        expected = np.array([10.0, 2.82842712, 2.0, 2.82842712])
        actual = genMagSpec(np.array([1,2,3,4]))
        print expected
        print actual
        self.assertTrue(np.isclose(expected, actual).all())

if __name__ == '__main__':
    unittest.main()
