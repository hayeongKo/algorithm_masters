# 3085
# 사탕 게임

import sys

input = sys.stdin.readline
spaces= []


N = int(input())

for _ in range(N):
    spaces.append(list(input().rstrip()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def checkMaxCandy(spaces):
    maxN = 0
    for i in range(N):
        # 행
        cnt = 1
        for j in range(1, N):
            if spaces[i][j] == spaces[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            maxN = max(cnt, maxN)
        # 열
        cnt = 1
        for j in range(1, N):
            if spaces[j][i] == spaces[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            maxN = max(cnt, maxN)

    return maxN
            
results = []
for i in range(N):
    for j in range(N):
        for k in range(4):
            if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:
                spaces[i][j], spaces[i+dx[k]][j+dy[k]] = spaces[i+dx[k]][j+dy[k]], spaces[i][j]
                answer = checkMaxCandy(spaces)
                results.append(answer)
                spaces[i+dx[k]][j+dy[k]], spaces[i][j] = spaces[i][j], spaces[i+dx[k]][j+dy[k]]

print(max(results))