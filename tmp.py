from functools import lru_cache
@lru_cache(None)
def f(n, r):
    if r == 1:
        return (n,),
    return tuple((i,) + comb for i in range(1, n) for comb in f(n - i, r - 1))
sum = 0
for i in range(1,31):
    sum += len(f(30,i))
print(sum)