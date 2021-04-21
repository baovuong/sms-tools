import os 
import sys 
import unittest
import numpy as np
from loadTestCases import load
import math

from A4Part1 import extractMainLobe 
from A4Part2 import computeSNR
from A4Part3 import computeEngEnv

class TestAssignment(unittest.TestCase):
    
    # Part 1
    def test_extractMainLobe1(self):
        result = extractMainLobe('blackmanharris', 100)
        self.assertEqual(65, result.size)

    def test_extractMainLobe2(self):
        result = extractMainLobe('boxcar', 120)
        self.assertEqual(17, result.size)

    def test_extractMainLobe3(self):
        result = extractMainLobe('hamming', 256)
        self.assertEqual(33, result.size)
    

    # Part 2
    def test_computeSNR1(self):
        result = computeSNR('../../sounds/piano.wav', 'blackman', 513, 2048, 128)
        self.assertAlmostEqual(67.57748352378475, result[0], delta=10)
        self.assertAlmostEqual(304.68394693221649,result[1], delta=100)

    def test_computeSNR2(self):
        result = computeSNR('../../sounds/sax-phrase-short.wav', 'hamming', 513, 1024, 64)
        self.assertAlmostEqual(89.510506656299285, result[0], delta=10)
        self.assertAlmostEqual(306.18696700251388,result[1], delta=100)


    def test_computeSNR3(self):
        result = computeSNR('../../sounds/rain.wav', 'hanning', 1024, 2048, 128)
        self.assertAlmostEqual(74.631476225366825, result[0], delta=10)
        self.assertAlmostEqual(304.26918192997738,result[1], delta=100)

    # Part 3
    def test_computeEngEnv1(self):
        result = computeEngEnv('../../sounds/piano.wav', 'blackman', 513, 1024, 128)
        print(result)
        self.assertEqual(69, result[:,0].size)
        self.assertEqual(163, result[:,1].size)

    def test_computeEngEnv2(self):
        result = computeEngEnv('../../sounds/piano.wav', 'blackman', 2047, 4096, 128)

    def test_computeEngEnv3(self):
        result = computeEngEnv('../../sounds/sax-phrase-short.wav', 'hamming', 513, 2048, 256)