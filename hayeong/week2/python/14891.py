import sys
from collections import deque

input = sys.stdin.readline

gears = []
gears.append([])
for _ in range(4):
    gears.append(deque(list(input().rstrip())))

K = int(input())

def rotate_left(index, rotate):
    cnt = 1
    for i in range(0, index-1):
        if gears[index-i][-3] != gears[index-i-1][2]:
            gears[index-i-1].rotate((-1)**cnt*rotate)
            cnt += 1
        else:
            return

def rotate_right(index, rotate):
    cnt = 1
    for i in range(index, 4):
        if gears[i][2] != gears[i+1][-3]:
            gears[i+1].rotate((-1)**(cnt)*rotate)
            cnt += 1
        else:
            return

for _ in range(K):
    index, rotate = map(int, input().split(" "))

    #회전
    gears[index].rotate(rotate)
    rotate_left(index, rotate)
    rotate_right(index, rotate)


answer = 0
for i in range(1, 5):
    if gears[i][0] == '1':
        answer += 2**(i-1)
print(answer)
    
for i in range(1, 5):
    print(gears[i])