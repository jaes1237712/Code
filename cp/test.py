import numpy as np
import matplotlib.pyplot as plt

N, L, V0, w = 80, 1., 10., 1.8
U = np.zeros((N+1,N+1))
U[N*1//4,N//4:N*3//4+1] = -V0
U[N*3//4,N//4:N*3//4+1] = +V0
for step in range(1000):
    max_delta = 0.
    for i in range(1,N):
        for j in range(1,N):
            if i==N*1//4 and j>=N//4 and j<=N*3//4: continue
            if i==N*3//4 and j>=N//4 and j<=N*3//4: continue
            delta = (U[i+1,j]+U[i-1,j]+U[i,j+1]+U[i,j-1])/4. - U[i,j]
            U[i,j] += w*delta
            if abs(delta)>max_delta: max_delta = abs(delta)
    print('Step: %3d, max_delta = %g' % (step,max_delta))
    if max_delta<1E-4: break
    
Ex, Ey = np.zeros((N+1,N+1)), np.zeros((N+1,N+1))
for i in range(1,N):
    for j in range(1,N):
        Ex[i,j] = -(U[i,j+1]-U[i,j-1])/(2.*L/N)
        Ey[i,j] = -(U[i+1,j]-U[i-1,j])/(2.*L/N)
    
fig = plt.figure(figsize=(6,6), dpi=80)
x = y = np.linspace(0.,L,N+1)
vx, vy = np.meshgrid(x,y)
plt.quiver(vx,vy,Ex,Ey)
plt.show()