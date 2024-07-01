import sys

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less, equal,greater = [], [], []
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return quick_sort(less) + equal + quick_sort(greater)

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

sorted_nums = quick_sort(nums)

sum = 0
for i in range(N):
    sum += sorted_nums[i]*(N-i)
print(sum)
