def f(n, a):
    nums = [4, 8, 15, 16, 23, 42]
    aux = [0] * 6

    for e in a:
        i = nums.index(e)
        if (i == 0):
            aux[i] += 1
        else:
            if (aux[i-1] > 0):
                aux[i-1] -= 1
                aux[i] += 1

    res = n - aux[5] * 6
    return res


n = int(input())
a = list(map(int, input().split()))
print(f(n, a))
