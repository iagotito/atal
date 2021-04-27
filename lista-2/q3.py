from itertools import permutations

def perfect(permuts):
    for p in permuts:
        for i in range(len(p)-1):
            is_perfect = True
            if p[i] != p[i+1]*3 and p[i] != p[i+1]/2:
                is_perfect = False
                break

        if is_perfect: return p


l = map(int, input().split())
permuts = list(permutations(l))

print(*perfect(permuts), sep=' ')
