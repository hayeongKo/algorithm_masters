import sys

input = sys.stdin.readline
leak, L = map(int, input().split())
lst_leak = list(map(int, input().split()))

lst_leak.sort()

start = lst_leak[0]
count = 1

for leak in lst_leak[1:]:
    if leak in range(start, start+L):
        continue
    else:
        start = leak
        count += 1

print(count)