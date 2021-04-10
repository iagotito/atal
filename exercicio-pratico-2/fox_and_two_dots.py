import sys

sys.setrecursionlimit(10000)


def cycle(x, y, px=-1, py=-1):
    vp.add((x, y))
    for mx, my in [(-1,0), (0,1), (1,0), (0, -1)]:
        nx = x+mx
        ny = y+my
        if nx >= 0 and nx < n and ny >= 0 and ny < m and \
        (nx, ny) != (px,py) and b[nx][ny] == b[x][y]:
            if (nx, ny) in vp or cycle(nx, ny, x, y):
                return True
    return False


n, m = map(int, input().split())
b = [input() for i in range(n)]
vp = set()

for i in range(n):
    for j in range(m):
        if not (i, j) in vp:
            if cycle(i, j):
                print('Yes')
                quit()
print('No')

