import struct
import matplotlib.pyplot as plt
import numpy as np
#If using termux
import subprocess
import shlex
#end if

N = 8    #N point FFT 
with open("fft_values.dat", "br") as f:
    buffer = f.read()
    real_X = []
    imag_X = []
    for i in range(N):
        real_X.append(struct.unpack('f', buffer[0+4*i:4*i+4]))
    for i in range(N,2*N):
        imag_X.append(struct.unpack('f', buffer[0+4*i:4*i+4]))    

X = np.array(real_X)+1j*np.array(imag_X)
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
#plt.show()
#If using termux
#plt.savefig('../figs/fft_c.pdf')
#plt.savefig('../figs/fft_c.eps')
subprocess.run(shlex.split("termux-open ../figs/fft_c.pdf"))
#else
#plt.show()