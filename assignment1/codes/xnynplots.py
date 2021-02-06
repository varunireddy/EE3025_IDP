import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if



x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
k = 15
y = np.zeros(15)


y[0] = x[0]
y[1] = -0.5*y[0]+x[1]

for n in range(2,k-1):
	if n < 6:
		y[n] = -0.5*y[n-1]+x[n]+x[n-2]
	elif n > 5 and n < 8:
		y[n] = -0.5*y[n-1]+x[n-2]
	else:
		y[n] = -0.5*y[n-1]

print("Maximum value of y(n) is ",np.max(y))
print("Minimum value of y(n) is ",np.min(y))
print("Maximum value of x(n) is ",np.max(x))
plt.figure(1)
plt.stem(range(0,6),x)
plt.title('Bounded Input')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid()
#If using termux
#plt.savefig('../figs/x_n.eps')
#plt.savefig('../figs/x_n.pdf')
subprocess.run(shlex.split("termux-open ../figs/x_n.pdf"))

plt.figure(2)
plt.stem(range(0,k),y)
plt.title('Bounded Output')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

#If using termux
#plt.savefig('../figs/y_n.pdf')
#plt.savefig('../figs/y_n.eps')
subprocess.run(shlex.split("termux-open ../figs/y_n.pdf"))
#else
#plt.show()
