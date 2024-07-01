import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

nums.sort()

start = 0
end = N-1

sum = nums[start] + nums[end]
answer = [nums[start], nums[end]]

while start < end:
    tmp = nums[start] + nums[end]

    if abs(tmp) < abs(sum):
        sum = tmp
        answer = [nums[start], nums[end]]
        if sum == 0:
            break

    if tmp < 0:
        start += 1
    else:
        end -= 1

print(answer[0], answer[1])