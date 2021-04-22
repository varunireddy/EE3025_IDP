import numpy as np
import cmath
from polypower import *


def add(x,y):
    m = len(x)
    n = len(y)
    if(m==n):
        return x+y
    elif m>n:
        return x + np.concatenate((np.zeros(m-n),y))
    else:
        return y + np.concatenate((np.zeros(n-m),x))

def bilin(p,om):
    N = len(p)
    const = np.array([1,-1])
    v = np.array([1])
    if N>2:
        for i in range(1,N):
            v = np.convolve(v,const)
            v = add(v,p[i]*polypower(np.array([1,1]),i))
        digden = v
        dignum = polypower(np.array([-1,0,1]),int((N-1)/2))
        G_bp = abs(np.polyval(digden,np.exp(-1j*om))/np.polyval(dignum,np.exp(-1j*om)))

    elif N==2:
        M = len(v)
        print(M)
        v[M-2] = v[M-2]+p[N-1]
        v[M-1] = v[M-1] + p[N-1]
        digden = v
        
        
    else:
        digden = p
        dignum = polypower(np.array([-1,0,1]),int((N-1)/2))
    
    dignum = polypower(np.array([-1,0,1]),int((N-1)/2))
    G_bp = abs(np.polyval(digden,np.exp(-1j*om))/np.polyval(dignum,np.exp(-1j*om)))
    return dignum,digden,G_bp
