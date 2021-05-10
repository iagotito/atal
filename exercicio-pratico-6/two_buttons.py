from collections import deque

n, m = map(int, input().split())


def f(n, m):
    g = dict()
    g[n] = [2 * n, n - 1]

    gd = dict()
    gd[n] = 0
    gd[2 * n] = 1
    gd[n - 1] = 1

    q = deque()
    q += g[n]

    while True:
        num = q.popleft()
        if num == m:
            return gd[num]
        elif num > m:
            g[num] = [num - 1]
        elif num < m / 10:
            g[num] = [num * 2]
        else:
            g[num] = [2 * num, num - 1]
        for v in g[num]:
            if gd.get(v) is None:
                gd[v] = gd[num] + 1
        q += g[num]


sum = 0
ma = m

if n < m:
    while True:
        m = ma
        ma = (ma + 1) // 2
        sum += f(ma, m)
        if ma / 2 < n:
            sum += f(n, ma)
            break
    print(sum)
else:
    print(f(n, m))
