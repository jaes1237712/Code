import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integral
 
f = lambda x : np.sqrt((1-2*x)/(2*x*(1-x)))
lb, ub = 0, 0.5
#result = integral.quad(f, lb, ub)
#print("The integration is {:.4f}".format(result[0]))
 
x = np.linspace(1E-10, 0.495, 10000)
z = (1+2*x-6*x**2)/(2*(1-2*x))
y = np.zeros(1)
for i in range(1,10000):
    y = np.append(y,integral.quad(f, lb, x[i])[0])
plt.plot(y, z)
plt.ylabel(r'$\dfrac{T}{mg}$')
plt.xlabel(r'$\tau$')
plt.grid(True, linestyle='--', which='major')
plt.savefig("test.png")
plt.show()