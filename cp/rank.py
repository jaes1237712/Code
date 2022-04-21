import numpy as np
import numpy.linalg as la

a = np.array([-1,-1,1,1])
ans = a
for i in range(4):
    for k in range(4):
        if i==k:
            continue
        for j in range(4):
            if j==k or j==i:
                continue
            for m in range(4):
                if m==j or m==k or m==i:
                    continue
                temp = np.array([a[i],a[k],a[j],a[m]])
                print(i,k,j,m)
                ans = np.vstack((ans,temp))
                
            

print(la.matrix_rank(ans))