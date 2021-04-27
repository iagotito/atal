def rm(n, d):
    m = -1
    for _ in range(d):
        for i in range(len(n)):
            c = n[i]
            if i == 0:
                m = c
                continue

            if c < m: m = c

        n.pop(n.index(m))

    return n


inpt = input().split()
n = list(inpt[0])
d = int(inpt[1])
print(*rm(n, d), sep='')
