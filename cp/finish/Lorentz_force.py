import numpy as np
from scipy.integrate import solve_ivp 

m,q = 1,1
E_field,B_field = [0,0,0], [0,0,0]
def f(t,pos):
    v = pos[3:6]
    a = E_field + (np.cross(v,B_field))
    return np.append(v,a)

def particle_positions(E, B):
    pos = np.array([0,0,0,0,0,0])     #[x,y,z,vx,vy,vz]
    positions = np.zeros(24)
    global E_field
    E_field = E
    global B_field
    B_field = B
    ### START YOUR CODE HERE ###
    for i in range(8):
        sol = solve_ivp(f,[0,i+1],pos,atol=1E-12, rtol=1E-12)
        for j in range(i*3,i*3+3):
            positions[j] = sol.y[j-i*3,-1]
    #### END YOUR CODE HERE ####
    return positions
print(particle_positions([0.13149066,-0.35713423,0.10541661] ,[0.00890957,-0.36257758,0.25168545]))