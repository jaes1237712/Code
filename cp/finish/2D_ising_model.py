import numpy as np

N = 10
kB = 1.0
J = 1.0

def Energy(S):
    E  = (S[:N-1,:]*S[1:,:]).sum() + (S[-1,:]*S[0,:]).sum()
    E += (S[:,:N-1]*S[:,1:]).sum() + (S[:,-1]*S[:,0]).sum()
    for i in range(N):
        for j in range(N):
                E += S[i][j]*S[(i-1)%N][(j+1)%10]
    sum = 0 
    for i in range(N):
        for j in range(N):
            sum += S[i][j]
    return E*(-J)-0.33*sum
def process(T):
    T = T
    for trial in range(1):
        Sk = np.ones((N,N))
        Ek = Energy(Sk)
        for it in range(1000):
            St = Sk.copy()
            St[np.random.randint(N),np.random.randint(N)] *= -1.
            Et = Energy(St)
            P = np.exp(-(Et-Ek)/kB/T)
            if P>=np.random.rand():
                Sk, Ek = St, Et
        return abs(Sk.sum())


def calc_magnetization_2D(T):
    M = 0.
    ### START YOUR CODE HERE ###
    for times in range(100):
        M += process(T)
    M /= 100
    #### END YOUR CODE HERE ####
    return float(M)
calc_magnetization_2D(8.6000)