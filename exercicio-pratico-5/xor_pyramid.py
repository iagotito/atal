n = int(input())
matrix = [[0] * n for i in range(n)]
g = [[0] * n for i in range(n)]

inpt = list(map(int, input().split()))

for i in range(n):
    matrix[i][i] = inpt[i]

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        a = matrix[i][j - 1]
        b = matrix[i + 1][j]
        xor = a ^ b
        matrix[i][j] = xor

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        a = matrix[i][j - 1]
        b = matrix[i + 1][j]
        matrix[i][j] = max(matrix[i][j], a, b)

m = int(input())
for i in range(m):
    query = list(map(int, input().split()))
    print(matrix[query[0] - 1][query[1] - 1])
