import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

min_num = 99999
min_difference = 9999999999

for i in range(N):
    difference = 0
    for j in range(N):
        difference += abs(nums[i] - nums[j])

    if min_difference > difference:
        min_difference = difference
        min_num = nums[i]
    elif min_difference == difference:
        if min_num > nums[i]:
            min_num = nums[i]

print(min_num)




