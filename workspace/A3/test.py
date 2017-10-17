import os
import unittest
import numpy as np
from loadTestCases import load

from A3Part1 import minimizeEnergySpreadDFT
from A3Part2 import optimalZeropad 
from A3Part3 import testRealEven
from A3Part4 import suppressFreqDFTmodel
from A3Part5 import zpFFTsizeExpt

class TestAssignment(unittest.TestCase):
    
    def test_minimizeEnergySpreadDFT1(self):
        testData = load(1, 1)
        mX = minimizeEnergySpreadDFT(testData['input']['x'], testData['input']['fs'], testData['input']['f1'], testData['input']['f2'])
        self.assertTrue(np.allclose(testData['output'], mX))
    def test_minimizeEnergySpreadDFT2(self):
        testData = load(1, 2)
        mX = minimizeEnergySpreadDFT(testData['input']['x'], testData['input']['fs'], testData['input']['f1'], testData['input']['f2'])
        self.assertTrue(np.allclose(testData['output'], mX))
        
    def test_optimalZeropad1(self):
        testData = load(2, 1)
        mX = optimalZeropad(testData['input']['x'], testData['input']['fs'], testData['input']['f'])
        self.assertTrue(np.allclose(testData['output'], mX))
    
    def test_optimalZeropad2(self):
        testData = load(2, 2)
        mX = optimalZeropad(testData['input']['x'], testData['input']['fs'], testData['input']['f'])
        self.assertTrue(np.allclose(testData['output'], mX))
    
    def test_testRealEven1(self):
        testData = load(3, 1)
        eIsRealEven, eDftbuffer, eX = testData['output']
        aIsRealEven, aDftbuffer, aX = testRealEven(testData['input']['x'])
        self.assertEquals(eIsRealEven, aIsRealEven);
        self.assertTrue(np.allclose(eDftbuffer, aDftbuffer))
        self.assertTrue(np.allclose(np.real(eX), np.real(aX)))
        self.assertTrue(np.allclose(np.imag(eX), np.imag(aX)))
    
    def test_testRealEven2(self):
        testData = load(3, 2)
        eIsRealEven, eDftbuffer, eX = testData['output']
        aIsRealEven, aDftbuffer, aX = testRealEven(testData['input']['x'])
        self.assertEquals(eIsRealEven, aIsRealEven);
        self.assertTrue(np.allclose(eDftbuffer, aDftbuffer))
        self.assertTrue(np.allclose(np.real(eX), np.real(aX)))
        self.assertTrue(np.allclose(np.imag(eX), np.imag(aX)))
    
    def test_suppressFreqDFTmodel1(self):
        data = load(4, 1)
        eY, eYfilt = data['output']
        aY, aYfilt = suppressFreqDFTmodel(data['input']['x'], data['input']['fs'], data['input']['N'])
        self.assertTrue(np.allclose(eY, aY))
        self.assertTrue(np.allclose(eYfilt, aYfilt))

    def test_suppressFreqDFTmodel2(self):
        data = load(4, 2)
        eY, eYfilt = data['output']
        aY, aYfilt = suppressFreqDFTmodel(data['input']['x'], data['input']['fs'], data['input']['N'])
        self.assertTrue(np.allclose(eY, aY))
        self.assertTrue(np.allclose(eYfilt, aYfilt))
        
    def test_zpFFTsizeExpt(self):
        data = load(5, 1)
        eMX1_80, eMX2_80, eMX3_80 = data['output']
        aMX1_80, aMX2_80, aMX3_80 = zpFFTsizeExpt(data['input']['x'], data['input']['fs'])
        self.assertTrue(np.allclose(eMX1_80, aMX1_80))
        self.assertTrue(np.allclose(eMX2_80, aMX2_80))
        self.assertTrue(np.allclose(eMX3_80, aMX3_80))
    
if __name__ == '__main__':
    unittest.main()
