import sys

input = sys.stdin.readline
H, W = map(int, input().split(" "))
heights = list(map(int, input().split()))

cnt = 0
contact = []
answer = 0

for i in range(H):
    y = H - i
    tmp = 0
    flag = -1 # 0: 왼쪽 막힘 1: 물 있음 -1:초기상태로
    for i in range(len(heights)):
        if heights[i] == y:
            heights[i] -= 1
            if flag == -1:
                flag = 0 #왼쪽 막힘
            if flag == 1: #오른쪽 막을거임
                answer += tmp
                flag = 1
                tmp = 0
        else:
            if flag == 0 or flag == 1:
                flag = 1
                tmp += 1
print(answer)