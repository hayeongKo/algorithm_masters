import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split(" ")))
queue = deque([])
result = []

for i in range(N):
    queue.append([i+1, nums[i]])

for _ in range(N):
    value = queue.popleft()
    queue.rotate(-value[1]+1 if value[1] > 0 else -value[1])
    print(value[0], end=" ")
