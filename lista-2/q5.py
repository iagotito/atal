import math

def cod(d):
    if(d == 1 or d == 0):
        return [d]
    else:
        l = cod(math.floor(d/2))
        l += cod(d%2)
        l += cod(math.floor(d/2))
    return l

d = int(input())
print(*cod(d), sep=' ')
