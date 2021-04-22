import numpy as np


def polypower(v,N):
    temp = np.array([1])
    if N>0:
        for i in range(1,N+1):
            temp = np.convolve(temp, v)
    return temp
