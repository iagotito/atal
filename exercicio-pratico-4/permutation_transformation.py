def tree(l, r, depth):
    if l > r: return
    
    m = max(a[l:r+1])
    mi = a.index(m)
    d[mi] = depth
    tree(l, mi-1, depth+1)
    tree(mi+1, r, depth+1)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = [0]*n
    tree(0, n-1, 0)
    print(*d, sep=' ')
