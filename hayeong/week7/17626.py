# 17625
# Four Squares

import sys

input = sys.stdin.readline
n = int(input())

# 가로 : 제곱수에 사용할 수 있는 수 (k**2 < n < (k+1)**2)
k = 1
while True:
    if k**2 > n:
        break
    else:
        k += 1

# 세로: 제곱수의 합으로 만들 자연수
dp = [[0]*(k+1) for _ in range(n+1)]

# 초기화
for j in range(k+1):
    dp[1][j] = 1

def determine_value(i):
    for j in range(1, k+1):
        if i == j**2: # 만들어야 하는 수가 제곱수인 경우
            for l in range(j, k+1):
                dp[i][l] = 1
            return
        else:
            sums = [4]
            if j != 1:
                sums.append(dp[i][j-1])
            p = 1
            while True:
                if i <= p**2:
                    break
                sums.append(dp[i-p**2][j]+dp[p**2][j])
                p += 1
            dp[i][j] = min(set(sums))

if n != 1:
    for i in range(2, n+1):
        determine_value(i)

for line in dp:
    print(line)

print(dp[n][k])
