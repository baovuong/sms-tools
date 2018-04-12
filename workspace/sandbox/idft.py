import numpy as np
import matplotlib.pyplot as plt


nv = np.arange([-N/2, N/2])
kv = np.arange([-N/2, N/2])

y = np.array([])
for n in nv:
    s = np.exp(1j * 2 * np.pi * n / N * kv)
    np.append(y, sum(X*s))
