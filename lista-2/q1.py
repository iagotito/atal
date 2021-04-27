def find_white_spaces(m, s):
    l = len(s)
    i = 0
    c = 0
    p = 'Vazio'

    while c < m:
        if i + m > l and s[i] != ' ': return 'Vazio'

        if s[i] == ' ':
            if c == 0: p = i
            c += 1
        else:
            c = 0
            p = 'Vazio'

        i += 1

    return p


m = int(input())
s = str(input())
print(str(find_white_spaces(m, s)))
