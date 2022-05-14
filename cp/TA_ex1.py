sum = 0 
def choose(used,seq):
    flag = 1
    for i in range(7):
        if used[i]:
            continue
        flag = 0
        tmp = used
        tmp[i] = 1
        choose(tmp,seq)