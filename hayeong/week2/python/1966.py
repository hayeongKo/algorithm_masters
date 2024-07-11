import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    N, M = map(int, input().split(" "))
    queue = deque(list(map(int, input().split())))
    answer = 1

    while True:
        maxmum = max(queue)
        pop = queue.popleft()

        if pop < maxmum:
            queue.append(pop)
            if M == 0:
                M = len(queue) - 1
            else:
                M -= 1
        else:
            if M == 0:
                print(answer)
                break
            else:
                answer += 1
                M -= 1


