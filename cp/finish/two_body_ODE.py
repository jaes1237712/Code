import math as m
import numpy as np 
from scipy.integrate import solve_ivp
# Initial condition
positions = np.zeros(8) # x1,y1,x2,y2,x1v,y1v...
t = 0
L_0 = 1
k = 100
m_1 = 0.5
m_2 = 1.0

# The length between two particle 
def L(pos):
    return m.sqrt((pos[0]-pos[2])**2+(pos[1]-pos[3])**2)
# p means prime

def f(t,pos):
    x1,y1,x2,y2 = pos[0],pos[1],pos[2],pos[3]
    vx1,vy1,vx2,vy2 = pos[4],pos[5],pos[6],pos[7]
    ax1 = (k/m_1)*(L(pos)-L_0)*((x2-x1)/L(pos))
    ay1 = (k/m_1)*(L(pos)-L_0)*(y2-y1)/L(pos)
    ax2 = (k/m_2)*(L(pos)-L_0)*(x1-x2)/L(pos)
    ay2 = (k/m_2)*(L(pos)-L_0)*(y1-y2)/L(pos)
    return np.array([vx1,vy1,vx2,vy2,ax1,ay1,ax2,ay2])

def twobody_positions(x1, y1, x2, y2, deltat):
    global positions
    positions = np.array([x1,y1,x2,y2,0.,0.,0.,0.])
    ### START YOUR CODE HERE ###
    sol = solve_ivp(f,[0, deltat], positions, atol =1E-12, rtol = 1E-12)
    #### END YOUR CODE HERE ####
    return sol.y[0:4,-1]

print(twobody_positions(0.636415, 0.930163, 0.837431, 1.03409, 5.35291))