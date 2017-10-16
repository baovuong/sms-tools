import os
import unittest
import numpy as np
from loadTestCases import load

from A3Part1 import minimizeEnergySpreadDFT

class TestAssignment(unittest.TestCase):
    def test_minimizeEnergySpreadDFT1(self):
        testData = load(1, 1)
        mX = minimizeEnergySpreadDFT(testData['input']['x'], testData['input']['fs'], testData['input']['f1'], testData['input']['f2'])
        print mX
        print testData['output']
        self.assertTrue(np.allclose(testData['output'], mX))
    def test_minimizeEnergySpreadDFT2(self):
        testData = load(1, 2)
        mX = minimizeEnergySpreadDFT(testData['input']['x'], testData['input']['fs'], testData['input']['f1'], testData['input']['f2'])
        self.assertTrue(np.allclose(testData['output'], mX))

if __name__ == '__main__':
    unittest.main()
