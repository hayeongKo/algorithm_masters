import sys

input = sys.stdin.readline
N = int(input())
output = []

for _ in range(N):
    left = []
    right = []
    for spell in input().removesuffix("\n"):
        if spell == '-':
            if left:
                left.pop()
        elif spell == '<':
            if left:
                right.append(left.pop())
        elif spell == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(spell)
    output.append(''.join(left)+''.join(reversed(right)))
    # print(''.join(left)+''.join(reversed(right)))
for result in output:
    print(result)
