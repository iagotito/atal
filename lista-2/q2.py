def rm(n, d):
    for _ in range(d):
        m = -1
        for i in range(len(n)-1):
            if n[i] <= n[i+1]:
                m = i
                break
        n.pop(m)
    return n


inpt = input().split()
n = list(inpt[0])
d = int(inpt[1])
print(*rm(n, d), sep='')
