from math import inf
from heapq import heappush, heappop


def shortest(graph, orig, dest):
    distances = {node: inf if node != orig else 0 for node in graph}
    queue = []
    for k, v in distances.items():
        heappush(queue, [v, k])

    while queue:
        weight, node = heappop(queue)

        for cn, cw in graph.get(node).items():
            new_weight = weight + cw
            if distances.get(cn) > new_weight:
                distances[cn] = new_weight

        for k, v in distances.items():
            for i in range(len(queue)):
                if queue[i][1] == k:
                    queue.pop(i)
                    heappush(queue, [v, k])

    return distances.get(dest)


c1, c2, m, n = input().split()
m = int(m)
n = int(n)

graph = {str(city+1): dict() for city in range(m)}
for _ in range(n):
    ci, cj, w = input().split()
    w = int(w)
    graph[ci][cj] = w

print(shortest(graph, c1, c2))
