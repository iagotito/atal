from math import inf


def shortest_with_negatives(nodes_qntd, edges, orig, dest):
    distances = {str(n+1): inf if str(n+1) != orig else 0 for n in range(nodes_qntd)}
    for _ in range(nodes_qntd-1):
        for n1, n2, w in edges:
            nw = distances[n1] + w
            if distances[n2] > nw:
                distances[n2] = nw

    for n1, n2, w in edges:
        if distances[n2] > distances[n1] + w:
            return False

    return distances.get(dest)


c1, c2, m, n = input().split()
m = int(m)
n = int(n)

edges = []
for _ in range(n):
    ci, cj, w = input().split()
    w = int(w)
    edges.append((ci, cj, w))

print(shortest_with_negatives(m, edges, c1, c2))
