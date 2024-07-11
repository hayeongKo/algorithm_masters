import sys
from itertools import combinations

input = sys.stdin.readline
sentence = list(input().rstrip())
left = []
right = []
answer = set()

tmp = ""
for i in range(len(sentence)):
    if sentence[i] == "(":
        left.append(i)
    elif sentence[i] == ")":
        right.append(i)
    else:
        tmp += sentence[i]

pairs = []
for i in range(len(left)):
    pairs.append([left[i], right[-i-1]])

for i in range(1, len(pairs)+1):
    for pair in list(combinations(pairs, i)):
        temp = list(sentence)
        for a, b in pair:
            temp[a] = ''
            temp[b] = ''
        answer.add(''.join(temp))


for word in sorted(answer):
    print(word)