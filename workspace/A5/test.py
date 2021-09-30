import os 
import sys 
import unittest
import numpy as np
from loadTestCases import load
import math

from A5Part1 import minFreqEstErr 

class TestAssignment(unittest.TestCase):
    
    # Part 1
    def test_minFreqEstErr1(self):
        result = minFreqEstErr('../../sounds/sine-490.wav', 490.0)
        self.assertAlmostEqual(result[0], 489.963, delta=0.001)
        self.assertEqual(result[1], 1101)
        self.assertEqual(result[2], 2048)

    def test_minFreqEstErr2(self):
        result = minFreqEstErr('../../sounds/sine-1000.wav', 1000.0)
        self.assertAlmostEqual(result[0], 1000.02, delta=0.001)
        self.assertEqual(result[1], 1101)
        self.assertEqual(result[2], 2048)

    def test_minFreqEstErr3(self):
        result = minFreqEstErr('../../sounds/sine-200.wav', 200.0)
        self.assertAlmostEqual(result[0], 200.038, delta=0.001)
        self.assertEqual(result[1], 1201)
        self.assertEqual(result[2], 2048)

if __name__ == '__main__':
    unittest.main()