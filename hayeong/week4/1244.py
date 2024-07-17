# 스위치 켜고 끄기

import sys

input = sys.stdin.readline
N = int(input()) # 스위치 개수
switches = list(map(int, input().split(" ")))
switches.insert(0, 0)
n_student = int(input())

for _ in range(n_student):
    gender, index = map(int, input().split())
    if gender == 1: #남자일 경우
        tmp = index
        while tmp <= N:
            switches[tmp] = 0 if switches[tmp] == 1 else 1
            tmp += index
    else: #여자일 경우
        front, rear = index, index
        while front != 0 and rear != N+1:
            if switches[front] == switches[rear]:
                if front == rear:
                    switches[front] = 0 if switches[front] == 1 else 1
                else:
                    switches[front] = 0 if switches[front] == 1 else 1
                    switches[rear] = 0 if switches[rear] == 1 else 1
                front, rear = front-1, rear+1
            else:
                break

for i in range(1, N+1):
    print(switches[i], end=" ")
    if i % 20 == 0:
        print()