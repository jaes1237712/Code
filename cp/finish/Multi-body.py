import math
import numpy as np 
from scipy.integrate import solve_ivp

# in the order of [mass, x, y, vx, vy]
init_data = np.array([[0.362, +0.380, -1.954, -2.364, +0.461],
                      [0.168, +0.032, +0.631, +0.233, -0.608],
                      [0.413, +0.280, -0.095, -0.672, -0.369],
                      [0.209, -1.669, +0.116, -1.965, +0.237],
                      [0.172, +0.376, +0.673, -0.370, +0.723],
                      [0.322, -0.583, +0.355, -0.405, +0.831],
                      [0.289, -0.619, -0.960, -0.525, -1.366],
                      [0.108, +0.626, -1.931, +0.276, +1.698],
                      [0.491, +0.499, +0.217, -1.237, +0.084],
                      [0.325, +0.781, +1.452, -0.295, -0.827]])



def f(t,pos):
    v = pos[20:40]      # [vx,vy]

    a = np.zeros(20)    
    for i in range(10): # a = [ax,0]
        ax = 0
        mi,xi,yi = init_data[i][0],pos[i],pos[i+10] 
        for j in range(10):
            if j==i:
                continue
            mj,xj,yj = init_data[j][0],pos[j],pos[j+10]
            R = np.sqrt((xj-xi)**2+(yj-yi)**2)
            ax += (mj/R**2)*(xj-xi)/R
        a[i] = ax
    
    for i in range(10): # a = [ax,ay]
        ay = 0
        mi,xi,yi = init_data[i][0],pos[i],pos[i+10] 
        for j in range(10):
            if j==i:
                continue
            mj,xj,yj = init_data[j][0],pos[j],pos[j+10]
            R = np.sqrt((xj-xi)**2+(yj-yi)**2)
            ay += (mj/R**2)*(yj-yi)/R
        a[i+10] = ay
    return np.append(v,a) #[vx,vy,ax,ay]

def multibody_positions(deltat):
    # Initial 
    positions = np.zeros(40)                # in the order of [x,y,vx,vy]
    for i in range(10):                     # positions = [x,0,0,0]
        positions[i] = init_data[i][1]      
    for i in range(10):                     # positions = [x,y,0,0]
        positions[10+i] = init_data[i][2]
    for i in range(10):                     # positions = [x,y,vx,0]
        positions[20+i] = init_data[i][3]
    for i in range(10):                     # positions = [x,y,vx,vy]
        positions[30+i] = init_data[i][4]
    ### START YOUR CODE HERE ###
    solve = solve_ivp(f,[0,deltat], positions, atol=1E-12, rtol=1E-12)
    #### END YOUR CODE HERE ####
    return solve.y[0:20,-1]

print(multibody_positions(0.088146))
