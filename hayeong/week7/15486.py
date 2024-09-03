# 15486
# 퇴사 2

import sys

input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)

for i in range(1, N+1):
    T, P = map(int, input().split())
    dp[i] = max(dp[i-1], dp[i])

    if (i-1)+T <= N:
        dp[i-1+T] = max(dp[i-1] + P, dp[i+T-1])

print(dp[N])