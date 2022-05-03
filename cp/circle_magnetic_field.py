from vpython import *
import numpy as np
import matplotlib.pyplot as plt

# cylinder magnet (r,theta,z) r in [0,1], theta in [0,2pi], z in [-1,0]
# semiconductor's initial position (0,0,0.25)
unit_m = vector(0,0,100*-72.98616758*15.27590689) # a unit of magnetic dipole
mu_0 = 4*pi*10E-9 # Vacuum permeability (SI units but change m to cm)
list_z = [0.01,0.02,0.03,0.04,0.05,0.07,0.1,0.14,0.2,0.28,0.4,0.57,0.8,1.13,1.6,2.3,3.2,4.5,6.4,9,12.5,18,25,35,50]
def get_B_field(m,r): # A(B-C)
    A = mu_0/(4*pi)
    B = 3*r*(dot(m,r))/pow(mag(r),5)
    C = m/pow(mag(r),3)
    return A*(B-C)

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

B_field = zerolistmaker(len(list_z))
for itr in range(len(list_z)):
    z = vector(0,0,list_z[itr]/10+0.25)
    for i in range(21): # slice z in [-1,0] 
        for j in range(21): # slice r in [0,1] delta_r = const
            for k in range(4*j):
                delta_theta = (2*pi)/(4*j)
                r = j/20
                theta = delta_theta*k
                r_m = vector(r*cos(theta), r*sin(theta), -i/20)
                #arrow(pos=r_m,axis=unit_m/100, shaftwidth=0,color=color.blue)
                B_field[itr] += get_B_field(unit_m,z-r_m).z 
print(B_field)       
B_field = np.array(B_field)
list_z = np.array(list_z)
plt.plot(np.log(list_z), np.log(-1*B_field),'o-')
plt.show()