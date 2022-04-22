import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp

fig = plt.figure(figsize=(6,6), dpi=80)
ax = plt.axes(xlim=(-1.2,+1.2), ylim=(-1.2,+1.2))

spring, = ax.plot([], [], lw=2, color='black')
ball,  = ax.plot([], [], 'ro', ms=10)
text   = ax.text(0.,1.1,'', fontsize = 16, color='black', ha='center', va='center')

m, g, R0, k = 1., 9.8, 0.5, 100.
t = 0.
y = np.array([0.3,0.4,0.,0.])

def f(t,y):
    bx, by = y[0], y[1]
    vx, vy = y[2], y[3]
    R = (bx**2+by**2)**0.5
    
    fs = -k*(R-R0)
    ax = fs*bx/R/m
    ay = fs*by/R/m - g
    
    return np.array([vx,vy,ax,ay])
    
def init():
    spring.set_data([], [])
    ball.set_data([], [])
    text.set(text='')
    return spring, ball, text

def animate(i):
    global t,y

    sol = solve_ivp(f, [t, t+0.040], y, atol = 1E-12, rtol = 1E-12)
    y   = sol.y[:,-1]
    t   = sol.t[-1]

    bx, by = y[0], y[1]
    vx, vy = y[2], y[3]
    R = (bx**2+by**2)**0.5
    npoints = 16
    sx = [0.]+[bx*i/(npoints-1)+(0.5-(i%2))*(by/R)*0.1 for i in range(1,npoints-1)]+[bx]
    sy = [0.]+[by*i/(npoints-1)-(0.5-(i%2))*(bx/R)*0.1 for i in range(1,npoints-1)]+[by]
    spring.set_data(sx, sy)
    ball.set_data(bx, by)
    
    E = m*g*by + 0.5*m*(vx**2+vy**2) + 0.5*k*(R-R0)**2
    text.set(text='E = %.16f' % E)

    return spring, ball, text

anim = animation.FuncAnimation(fig, animate, init_func=init,frames=10, interval=40)
plt.show()