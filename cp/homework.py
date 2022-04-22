import numpy as np
import math 
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
positions = init_data
who = 0
def f(t,pos):
    [m,x,y,vx,vy] = pos.copy()
    ax = 0
    ay = 0
    for k in range(10):
        if k==who:
            continue
        [mj,xj,yj,vxj,vyj] = positions[k].copy()
        R = math.sqrt((xj-x)**2+(yj-y)**2)
        ax += (mj/R**2)*(xj-x)/R
        ay += (mj/R**2)*(yj-y)/R
    value = [m,vx,vy,ax,ay]
    return value


def multibody_positions(deltat):
    global positions,who
    positions = init_data
    ### START YOUR CODE HERE ###
    dt = deltat/1000
    t = 0
    while t<deltat:
        pos = positions.copy()
        for i in range(10):
            who = i 
            sol = solve_ivp(f, [t,t+dt], positions[i])
            pos[i] = sol.y[:,-1]
        positions = pos
        t += dt
    #### END YOUR CODE HERE ####
    pos = np.array([positions[0][1]])
    for i in range(10):
        if i!=0:
            pos = np.append(pos,positions[i][1])
    for i in range(10):
        pos = np.append(pos,positions[i][2])
    return pos
    
print(multibody_positions(0.099701))