import numpy as np

N = 10
kB, T = 1.0, 1.0
J = 1.0

def Energy(S):
    E  = (S[:N-1,:]*S[1:,:]).sum() + (S[-1,:]*S[0,:]).sum()
    E += (S[:,:N-1]*S[:,1:]).sum() + (S[:,-1]*S[:,0]).sum()
    return E*(-J)

smp_E, smp_M = [], []
for trial in range(100):
    Sk = np.ones((N,N))
    Ek = Energy(Sk)
    for it in range(N*N*20):
        St = Sk.copy()
        St[np.random.randint(N),np.random.randint(N)] *= -1.
        Et = Energy(St)
        P = np.exp(-(Et-Ek)/kB/T)
        if P>=np.random.rand():
            Sk, Ek = St, Et
    Mk = abs(Sk.sum())
    smp_E.append(Ek);
    smp_M.append(Mk);
smp_E, smp_M = np.array(smp_E), np.array(smp_M)
print('kBT = %g, U = %g, C = %g, M = %g' % (kB*T, smp_E.mean(), smp_E.std()/kB/T**2, smp_M.mean()))