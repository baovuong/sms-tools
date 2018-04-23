import numpy as np 
from scipy.signal import get_window 
from scipy.fftpack import fft 
import math 
import matplotlib.pyplot as plt 

# === defining the window === 
M = 63                             # window length
window = get_window('hanning', M)  # window name/type
hM1 = int(math.floor((M + 1) / 2)) # middle of window (odd) 
hM2 = int(math.floor(M/2))         # middle of window (even)


# === to place window at zeroth location ===
N = 512                          # fft size we want (in samples)
hN = N/2 + 1
fftbuffer = np.zeros(N)          # buffer for fft 
fftbuffer[:hM1] = window[hM2:]   # place window around zeroth sample (right side)
fftbuffer[N-hM2:] = window[:hM2] # place window around zeroth sample (left side)

# === computing FFT ===
X = fft(fftbuffer)                                     # computed FFT
absX = abs(X)                                          # absolute values of FFT
absX[absX < np.finfo(float).eps] = np.finfo(float).eps # have any values below the minimum value  
                                                       # (which is eps, minium value we can have in python) equal the minimum value
mX = 20 * np.log10(absX)                               # convert to decibels to get magnitude spectrum
pX = np.angle(X)                                       # phase spectrum 

mX1 = np.zeros(N)
pX1 = np.zeros(N)
mX1[:hN] = mX[hN:]
mX1[N-hN:] = mX[:hN]
pX1[:hN] = pX[hN:]
pX1[N-hN:] = pX[:hN]
