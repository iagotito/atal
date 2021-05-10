def fa(p):
    if p != root[p]:
            root[p] = fa(root[p])
    return root[p]


n, m, k = map(int, input().split())
special = map(int, input().split())

root = [p for p in range(n+1)]

for i in range(m):
	u,v = map(fa, map(int, input().split()))
	root[v] = u

sz = [0 for i in range(n+1)]

for i in range(n+1):
	sz[fa(i)] += 1

leftover = n
ans = 0
largest = 0

for x in special:
	d = fa(x)
	largest = max(largest, sz[d])
	ans += sz[d] * (sz[d] - 1) // 2
	leftover -= sz[d]

ans -= largest * (largest - 1) // 2
ans += (largest+leftover) * ((largest+leftover) - 1) // 2
ans -= m

print(ans)
