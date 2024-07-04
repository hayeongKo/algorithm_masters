import sys

input = sys.stdin.readline
N = int(input())

cond_nums = []
for _ in range(N):
    cond_nums.append(int(input()))

stack = [0]
result = []
index = 1

for num in cond_nums:
    if num < stack[-1]:
        result.append("NO")
        break
    elif num == stack[-1]:
        stack.pop()
        result.append('-')
    else: 
        while True:
            if index <= num:
                stack.append(index)
                result.append('+')
                index += 1
            else:
                break
        if num == stack[-1]:
            stack.pop()
            result.append('-')

if result[-1] == "NO":
    print("NO")
else:
    for i in result:
        print(i)