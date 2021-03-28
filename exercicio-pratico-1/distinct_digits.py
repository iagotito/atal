num, max_num = map(int, input().split())
digits = [0]*10

while num <= max_num:
    check = num
    while check:
        if not digits[check % 10]:
            digits[check % 10] = 1
            check = check//10 
        else:
            check = 1
            break
    if not check: break
    num += 1
    digits = [0]*10

print(num if not check else -1)
