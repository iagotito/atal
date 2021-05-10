def find_cycles(graph):
    cycles = []
    for v1 in graph:
        for v2 in graph[v1]:
            for j1 in graph[v2]:
                if (j1 in graph[v1]):
                    cycles.append((v1, v2, j1))
    return cycles


def f(graph):
    cycles = find_cycles(graph)
    if (len(cycles) == 0):
        return -1
    min = 10**5
    for c in cycles:
        total = 0
        for v in c:
            total += len(graph[v]) - 2
        if (total < min):
            min = total
    return min


n, m = map(int, input().split())
graph = {}

for i in range(1, n+1):
    graph[i] = []
for i in range(m):
    origin, destiny = map(int, input().split())
    graph[origin].append(destiny)
    graph[destiny].append(origin)

print(f(graph))
