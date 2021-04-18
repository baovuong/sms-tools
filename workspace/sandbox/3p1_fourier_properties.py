import numpy as np
from scipy.signal import triang 
from scipy.fftpack import fft 

# signal
x = triang(15)

# buffer for symmetry
fftbuffer = np.zeros(15)
fftbuffer[:8] = x[7:]
fftbuffer[8:] = x[:7]

# dft (real and complex)
X = fft(fftbuffer)

# magnitude spectrum
mX = abs(X)

# phase spectrum
pX = np.angle(X)
