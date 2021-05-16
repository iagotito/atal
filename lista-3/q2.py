def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True


def f(n):
    n += 1
    s = []
    count = 0
    for i in range(3, n+1, 2):
        if is_prime(i): s.append(i)
    i = 0
    while i < len(s) and int(s[i]) < n:
        if i < len(s)-1 and s[i+1] - s[i] == 2:
            count += 1
        elif i > 0 and s[i] - s[i-1] == 2:
            count += 1
        i += 1
    return count


n = int(input())
print(f(n))
