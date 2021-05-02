def f(a):
  max_a = max(a) + 1
  dp = [0] * max_a

  for i in a:
    dp[i] += 1

  for i in range(2, max_a):
    dp[i] = max(dp[i-1], dp[i-2] + (dp[i]*i))

  return dp[-1]


n = input()
a = list(map(int, input().split()))

print(f(a))
