import sys

input = sys.stdin.readline
problem = list(input().rstrip())

stack = []

answer = 0
tmp = 1

for i in range(len(problem)):
    if problem[i] == '(':
        stack.append(problem[i])
        tmp *= 2
    elif problem[i] == '[':
        stack.append(problem[i])
        tmp *= 3
    elif problem[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if problem[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //=  2
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if problem[i-1] =='[':
            answer += tmp
        stack.pop()
        tmp //= 3 

if stack:
    print(0)
else:
    print(answer)
            