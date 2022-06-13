import numpy as np
import matplotlib.pyplot as plt
h = 6.626E-34
c = 3E8
k = 1.38E-23
T = 3000
x = np.linspace(0,3E-6,101)
nu = c/x
y = -1*((8*np.pi*h)/(x**3)) * (1/(1-np.exp((h*c/(k*T*x))))) * (h/(x**2))
plt.plot(x,y,'r')
T = 4000
y = -1*((8*np.pi*h)/(x**3)) * (1/(1-np.exp((h*c/(k*T*x))))) * (h/(x**2))
plt.plot(x,y,'g')
T = 5000
y = -1*((8*np.pi*h)/(x**3)) * (1/(1-np.exp((h*c/(k*T*x))))) * (h/(x**2))
plt.plot(x,y,'b')
plt.legend(['3000K','4000K','5000K'])
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$u(\lambda)$')