import os
import sys 
import unittest
import numpy as np
from A1Part1 import readAudio
from A1Part2 import minMaxAudio 
from A1Part3 import hopSamples
from A1Part4 import downsampleAudio

class TestAssignment(unittest.TestCase):

    def test_readAudio(self):
        expected = np.array([
            -0.06213569, 
            -0.04541154, 
            -0.02734458, 
            -0.0093997,
            0.00769066,
            0.02319407,
            0.03503525,
            0.04309214,
            0.04626606,
            0.0441908])
        actual = readAudio(os.path.join(os.path.dirname(sys.path[0]), 'sounds', 'piano.wav'))
        self.assertTrue(np.isclose(expected, actual).all())

    def test_minMaxAudio(self):
        expected = (-0.83486432, 0.56501967)
        actual = minMaxAudio(os.path.join(os.path.dirname(sys.path[0]), 'sounds', 'oboe-A4.wav'))
        self.assertEqual(round(expected[0], -3), round(actual[0], -3))
        self.assertEqual(round(expected[1], -3), round(actual[0], -3))

    def test_hopSamples(self):
        expected = np.array([0, 2, 4, 6, 8])
        actual = hopSamples(np.arange(10), 2)
        results = expected == actual
        print(results)
        self.assertTrue(results.all())

    def test_downsampleAudio(self):
        oldPath = os.path.join(os.path.dirname(sys.path[0]), 'sounds', 'vibraphone-C6.wav')
        newPath = os.path.join(os.path.dirname(sys.path[0]), 'sounds', 'vibraphone-C6_downsampled.wav')
        downsampleAudio(oldPath, 5)
        self.assertTrue(os.path.isfile(newPath))

if __name__ == '__main__':
    unittest.main()
