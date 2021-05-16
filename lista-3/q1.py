def f(s, x, y):
    r = [0] * len(s)
    for i in range(x, y):
        if s[i] == s[i+1]:
            r[i] = 1
    return r


s, x, y = input().split()
s = [e for e in s]
x = int(x) - 1
y = int(y) - 1

r = f(s, x, y)
print(sum(r))
