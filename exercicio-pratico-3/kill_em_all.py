s = ''
q = int(input())
for _ in range(q):
    n, r = map(int, input().split())
    p = sorted(set(map(int, input().split())), reverse=True)
 
    count = 0
    while count < len(p):
        if p[count] <= count*r: break
        count += 1
    s += str(count)+'\n'
print(s)
