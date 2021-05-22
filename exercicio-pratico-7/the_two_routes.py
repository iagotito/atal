cx, cy = map(int, input().split())
 
cross = [0] * (cx + 1)
for l in range(cx + 1):
    cross[l] = [1] * (cx + 1)
for i in range(cy):
    a, b = map(int, input().split())
    cross[a][b] = cross[b][a] = 2
x, v, i = 3 - cross[1][cx], [0] * (cx + 1), 1
d = [cx + 1] * (cx + 1)
t =  d[1] = 0
 
while i != cx:
    v[i] = 1
    for j in range(1, cx + 1):
        if v[j] == 0 and cross[i][j] == x and d[j] > d[i] + 1:
            d[j] = d[i] + 1
    m = cx + 1
    for j in range(1, cx + 1):
        if v[j] == 0 and d[j] < m:
            m = d[j]
            i = j
    if m == cx + 1:
        t = -1
        break
    elif i == cx:
        t = d[cx]
        break
 
print(t)
