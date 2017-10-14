import os
import unittest
import numpy as np
from loadTestCases import load

from A3Part1 import minimizeEnergySpreadDFT

class TestAssignment(unittest.TestCase):

    def test_minimizeEnergySpreadDFT1(self):
        testData = load(1, 1)
        mX = minimizeEnergySpreadDFT(testData['input'], 10000, 80, 200)
        self.assertEquals(len(mX), 126)
        self.assertTrue(all([mX[i] == 0 for i in range(len(mX)) if i != 80 and i != 200]))
        self.assertTrue(all([mX[i] > 0 for i in range(len(mX)) if i == 80 or i == 200]))
    def test_minimizeEnergySpreadDFT2(self):
        pass

if __name__ == '__main__':
    unittest.main()
