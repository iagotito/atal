cost, digit = map(int, input().split())

quant = 1
total_cost = cost
while total_cost % 10 != digit and total_cost % 10 != 0:
    total_cost += cost
    quant += 1

print(quant)
