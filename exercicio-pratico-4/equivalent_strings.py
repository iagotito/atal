def eq(s):
    if len(s) % 2: return s

    a = eq(s[:len(s)//2])
    b = eq(s[len(s)//2:])
    
    return a + b if a < b else b + a


a = str(input())
b = str(input())
print('YES' if eq(a) == eq(b) else 'NO')
