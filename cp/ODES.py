import math as m 
def f(t,y): 
    return y

t, y = 0., 1.
h = 1E-4
while t<=1-h:
    k1 = f(t,y)
    k2 = f(t+h/2,y+(h/2)*k1)
    k3 = f(t+h/2,y+(h/2)*k2)
    k4 = f(t+h, y+h*k3)  
    y += h*(k1+2*k2+2*k3+k4)/6
    t += h
print("VALUE:",y)
print("diff:",y-m.exp(t))