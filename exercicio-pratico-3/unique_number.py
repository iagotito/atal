for t in range(int(input())):
    s = ''
    x = int(input())
    for i in range(9, 0, -1):
        if x >= i:
            x -= i
            s = str(i) + s
    print(s if x == 0 else -1)
