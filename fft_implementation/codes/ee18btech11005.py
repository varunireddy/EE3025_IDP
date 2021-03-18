from cmath import exp, pi
import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    #D = np.zeros((N//2),dtype="complex")
    T =[exp(-2j * pi * k / N) * odd[k] for k in range(N // 2)]
    #print(T)
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

X = fft([1,2,3,4,4,3,2,1])
plt.figure(figsize=(7,8))
plt.subplot(2,1,1)
plt.grid()
plt.title("Magnitude Spectrum")
plt.ylabel("|X(k)|")
plt.stem(np.abs(X),use_line_collection=True)


plt.subplot(2,1,2)
plt.grid()
plt.title("Phase Spectrum")
plt.xlabel("k")
plt.ylabel(r'$\angle{H(k)}$')
plt.stem(np.angle(X),use_line_collection=True)
#If using termux
#plt.savefig('../figs/fft_py.pdf')
#plt.savefig('../figs/fft_py.eps')
subprocess.run(shlex.split("termux-open ../figs/fft_py.pdf"))
#else
#plt.show()