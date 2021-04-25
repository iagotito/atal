def good(l,c):
    ch = chr(c)
    if len(l) == 1: return 1 if ch != l[0] else 0
    x = len(l)//2
    lm = x-l[:x].count(ch) + good(l[x:],c+1)
    rm = x-l[x:].count(ch) + good(l[:x],c+1)
    return min(lm, rm)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(good(s, ord('a')))
