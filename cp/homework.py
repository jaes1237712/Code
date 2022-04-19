import numpy as np
L_0 = 1
k = 100
m_1 = 0.5
m_2 = 1.0

def acceleration(position):
    x1 = position[0]
    y1 = position[1]
    x2 = position[2]
    y2 = position[3]
    L = np.sqrt((x2-x1)**2+(y1-y2)**2)
    value = np.zeros(4)
    value[0] = (k/m_1)*(L-L_0)*((x2-x1)/L)
    value[1] = (k/m_1)*(L-L_0)*((y2-y1)/L)
    value[2] = (k/m_2)*(L-L_0)*((x1-x2)/L)
    value[3] = (k/m_2)*(L-L_0)*((y1-y2)/L)
    return value

def velocity_change(v,a,dt):
    temp = v
    for i in range(4):
        temp[i] += a[i]*dt
    return temp
def positions_change(x,v,dt):
    temp = x 
    for i in range(4):
        temp[i] += v[i]*dt
    return temp
    
def twobody_positions(x1, y1, x2, y2, deltat):
    positions = np.array([x1,y1,x2,y2])
    ### START YOUR CODE HERE ###
    a = acceleration(positions)
    v = np.zeros(4)
    dt = 1E-3
    t = 0
    while t<=deltat:
        positions = positions_change(positions, v, dt)
        v = velocity_change(v,a,dt)
        a = acceleration(positions)
        t += dt
    #### END YOUR CODE HERE ####
    return positions