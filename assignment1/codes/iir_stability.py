import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline
from collections import defaultdict

# Plot the complex z-plane given zeros and poles

def zplane(z, p):    
	"""
	z = list of zeros
	p = list of poles
	
	"""
	
    ax = plt.subplot(111)
    # Add unit circle and zero axes    
    unit_circle = patches.Circle((0,0), radius=1, fill=False,color='black', ls='dashed')
    ax.add_patch(unit_circle)
    axvline(0, color='0.7')
    axhline(0, color='0.7')

    # Plot the poles and set marker properties
    poles = plt.plot(p.real, p.imag, 'x', color = 'red',markersize=9)
    
    # Plot the zeros and set marker properties
    zeros = plt.plot(z.real, z.imag,  'o', markersize=9,color='None',markeredgecolor=poles[0].get_color())
    
    # Scale axes to fit
    r = 1.5 * np.amax(np.concatenate((abs(z), abs(p), [1])))              
    x = np.linspace(-2,2,100)  
    
    #Coloring the Roc      
    y1 = np.sqrt(16-x**2)
    y2 = -np.sqrt(16-x**2)
    plt.fill_between(x, y1, y2, color='#539ecd')
    roc = patches.Circle((0,0), radius=0.5, fill=True,color='white', ls='solid')
    ax.add_patch(roc)
    boundary = patches.Circle((0,0), radius=0.5, fill=False,color='black', ls='solid')
    ax.add_patch(boundary)
    plt.text(0,0.1,"z=0")
    plt.text(0.2,0.6,"|z|>0.5")
    plt.text(0,1.1,"|z|=1")
    plt.axis('scaled')
    plt.axis([-r, r, -r, r])
    plt.title("H(z) in z-plane")
    #plt.savefig('ee18btech11005.pdf')
    #plt.savefig('ee18btech11005.eps')
    plt.show()


zplane(np.array([-1j,1j]),np.array([-0.5,0]))
