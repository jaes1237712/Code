import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

x,y = np.meshgrid(np.linspace(-10,10,10),np.linspace(-10,10,10))

u = 1
v = -1

plt.quiver(x,y,x,-y)
plt.show()