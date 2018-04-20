import os 
import sys 
import unittest
import numpy as np
from loadTestCases import load
import math

from A4Part1 import extractMainLobe 

class TestAssignment(unittest.TestCase):
    
    def test_extractMainLobe1(self):
        result = extractMainLobe('blackmanharris', 100)
        self.assertEqual(65, result.size)

    def test_extractMainLobe2(self):
        result = extractMainLobe('boxcar', 120)
        self.assertEqual(17, result.size)

    def test_extractMainLobe3(self):
        result = extractMainLobe('hamming', 256)
        self.assertEqual(33, result.size)