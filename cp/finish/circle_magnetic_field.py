from vpython import *
import numpy as np
import matplotlib.pyplot as plt

# cylinder magnet (r,theta,z) r in [0,1], theta in [0,2pi], z in [-1,0]
# semiconductor's initial position (0,0,0.25)
unit_m = vector(0,0,1000) # a unit of magnetic dipole
mu_0 = 4*pi*10E-9 # Vacuum permeability (SI units but change m to cm)
list_z = [-15,-13.5,-12.5,-11,-10,-9,-8,-7,-6,-5,-3,-2.7,-2.6,-2.5,-1.5,-1,0]
list_z_0 = [0.01,0.02,0.03,0.04,0.05,0.07,0.1,0.14,0.2,0.28,0.4,0.57,0.8,1.13,1.6,2.3,3.2,4.5,6.4,9,12.5,18,25,35,50]
list_B = [-19.99300245,-19.99300245,-19.99300245,-19.99300245,-19.99300245,-19.99300245,-19.99300245,-19.99300245,-19.99300245,-19.74308992,-19.39321238,-19.04333483,-18.44354476,-17.74378967,-16.69415705,-15.19468186,-13.59524167,-11.4459939,-8.996851102,-6.547708302,-4.398460539,-1.54945769,-0.799720098,-0.3498775429,-0.09996501225]
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
    for i in range(41): # slice z in [-1,0] 
        for j in range(41): # slice r in [0,1] delta_r = const
            for k in range(4*j):
                delta_theta = (2*pi)/(4*j)
                r = j/40
                theta = delta_theta*k
                r_m = vector(r*cos(theta), r*sin(theta), -i/40)
                #arrow(pos=r_m,axis=unit_m/100, shaftwidth=0,color=color.blue)
                B_field[itr] += get_B_field(unit_m,z-r_m).z 
B_field_circuit = zerolistmaker(len(list_z))

for itr in range(len(list_z)):              # B(z)= (mu_0 i R^2)/(2(R^2+z^2)^{3/2})
    d = list_z[itr]/10+0.25
    for i in range(5001):
        z = d+i/5000
        I,R = 10000, 1
        B_field_circuit[itr] += (mu_0*I*pow(R,2))/(2*(R**2+z**2)**(3/2))

B_field = np.array(B_field)# * (-19.99300245/B_field[0])
B_field_circuit = np.array(B_field_circuit)*-1#* (-19.99300245/B_field_circuit[0])
list_z = np.array(list_z)
list_B = np.array(list_B)
# plt.plot(np.log(list_z), np.log(abs(B_field)),'o-')
# plt.plot(np.log(list_z_0), np.log(abs(list_B)),'ro-')
# plt.plot(np.log(list_z), np.log(abs(B_field_circuit)),'go-')
# plt.legend(["Simulation by dipoles","Experiment","Simulation by circuit"])
# plt.xlabel("$\ln{z}$", color='pink')
# plt.ylabel("$\ln{B}$", color='pink')
plt.plot(list_z,B_field,'o-')
plt.plot(list_z,B_field_circuit,'go-')
plt.legend(["Simulation by dipoles","Simulation by circuit"])
plt.xlabel("$z$", color='pink')
plt.ylabel("$B$", color='pink')
plt.show()