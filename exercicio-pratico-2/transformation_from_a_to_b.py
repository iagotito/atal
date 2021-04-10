def op1(x):
    return 2*x


def op2(x):
    return 10*x + 1


def transform(a, b, transformations=[]):
    current_transformations = transformations + [a]

    if a == b: return current_transformations
    if a > b: return False

    t1 = transform(op1(a), b, current_transformations)
    t2 = transform(op2(a), b, current_transformations)

    return t1 if t1 else t2


a, b = map(int, input().split())
t = transform(a, b)
if t:
    print('YES')
    print(len(t))
    print(*t)
else:
    print('NO')

