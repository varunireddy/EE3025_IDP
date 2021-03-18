import time
import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

def dft(x):
	n = len(x)
	X = np.zeros((n,n),dtype=np.complex128)
	for i in range(n):
		for j in range(n):
				X[i][j] += x[j]*(np.exp(-2j*np.pi*j/n)) 
	return X

def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    #D = np.zeros((N//2),dtype="complex")
    T =[np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    #print(T)
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

no_of_trails = 10
dft_time = np.zeros(no_of_trails)
fft_time = np.zeros(no_of_trails)

for i in range(no_of_trails):
	N = 2**i
	x = np.random.randint(1,10,size=N)
	t1 = time.time()
	X_d = dft(x)
	t2 = time.time()
	X = fft(x)
	t3 = time.time()
	dft_time[i] = t2-t1
	fft_time[i] = t3-t2
	
axis = 2**np.arange(no_of_trails)
plt.plot(axis, dft_time, label = 'DFT Computation Time')
plt.plot(axis, fft_time, label = 'FFT Computation Time')
plt.title('DFT vs FFT Computation Times')
plt.xlabel('N')
plt.ylabel('Time of execution (in s)')
plt.xscale('log', basex=2)
plt.grid()
plt.legend()
#plt.show()
#If using termux
#plt.savefig('../figs/comparetime.pdf')
#plt.savefig('../figs/comparetime.eps')
subprocess.run(shlex.split("termux-open ../figs/comparetime.pdf"))
#else
#plt.show()