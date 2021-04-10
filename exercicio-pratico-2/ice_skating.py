n=int(input())
d=0
xl=[]
yl=[]

for i in range(n):
    x,y=map(int,input().split())
    xl.append({x})
    yl.append({y})

for i in range(n-1):
    j = i+1
    while j < n:
        if xl[i] & xl[j] or yl[i] & yl[j]:
            xl[j] |= xl[i]
            yl[j] |= yl[i]
            break
        j+=1
        if j == n: d+=1

print(d)

