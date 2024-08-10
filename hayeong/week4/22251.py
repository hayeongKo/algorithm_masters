# 22251
# 빌런 호석

import sys

input = sys.stdin.readline
N, K, P, X = map(int, input().split(" "))

num_lst = [
    [1, 1, 1, 0, 1, 1, 1], #0
    [0, 0, 1, 0, 0, 1, 0], #1
    [1, 0, 1, 1, 1, 0, 1], #2
    [1, 0, 1, 1, 0, 1, 1], #3
    [0, 1, 1, 1, 0, 1, 0], #4
    [1, 1, 0, 1, 0, 1, 1], #5
    [1, 1, 0, 1, 1, 1, 1], #6
    [1, 0, 1, 0, 0, 1, 0], #7
    [1, 1, 1, 1, 1, 1, 1], #8
    [1, 1, 1, 1, 0, 1, 1], #9
]

reversal = [[] for _ in range(10)] # 반전에 필요한 수

for i in range(10):
    for j in range(10):
        tmp = 0
        for k in range(7):
            if num_lst[i][k] != num_lst[j][k]:
                tmp += 1
        reversal[i].append(tmp)

real = str(X).zfill(K) # 비어있는 곳에 0을 채워줌

# 깊이 | 남은 반전 횟수 | 현재 문자열
def dfs(depth, cnt, string):
    if depth == len(string):
        if int(string) == X: # 현재 층과 호석이가 만든 층이 같을 때 -> 안됨
            return 0
        elif 1 <= int(string) <= N: # 가능한 경우
            return 1
        else: # 그 외의 경우는 안됨
            return 0
    
    rst, cur = 0, int(string[depth]) # 바뀔 수 있는 수, 현재 수
    for i in range(10):
        if cur != i and (reversal[cur][i] <= cnt): # 남은 반전 횟수보다 크지 않으며, 현재 수와 바뀔 수가 같지 않으면 
            new_string = string[:depth] + str(i) + string[depth+1:] # 해당 깊이에 있는 수를 바꿈
            rst += dfs(depth+1, cnt-reversal[cur][i], new_string)

        elif cur == i: # 만약 현재 깊이에 있는 수와 바뀔 수가 같으면 반전 횟수에 영향이 없음
            rst += dfs(depth+1, cnt, string)

    return rst

print(dfs(0, P, real))
    