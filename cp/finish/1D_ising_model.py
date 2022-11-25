import numpy as np
import matplotlib.pyplot as plt
N = 40
J = 1.0
def Energy(S):
    E = -J * ((S[:N-1]*S[1:]).sum() + S[-1]*S[0]) - (J/4)*((S[:N-2]*S[2:]).sum() + S[-1]*S[1] + S[-2]*S[0])
    E -= 0.33*(S.sum())
    return E


def process(T):
    
    kB, T = 1.0, T

    Sk = np.ones(N) # start with all spin up
    Ek = Energy(Sk)
    for it in range(N*10):
        St = Sk.copy()
        St[np.random.randint(N)] *= -1.
        Et = Energy(St)
        P = np.exp(-(Et-Ek)/kB/T)
        if P>=np.random.rand():
            Sk, Ek = St, Et
    return Sk

def calc_magnetization(T):
    M = 0.
    ### START YOUR CODE HERE ###
    for steps in range(100):
        Sk = process(T)
        M += abs(Sk.sum())
    M /= 100
    #### END YOUR CODE HERE ####

    return float(M)
