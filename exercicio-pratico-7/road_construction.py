n,m = map(int,input().split())
a = [0] * (n+1)
i = 0
while i < m:
    j,k = map(int,input().split())
    a[j] = 1
    a[k] = 1
    i += 1
i = 1
while i <= n:
    if a[i] == 0:
        break
    i += 1
j = 1
print(n-1)
while j <= n:
    if j != i:
        print(j,i)
    j += 1
