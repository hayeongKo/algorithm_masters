import sys

def binarySearch(start, end, c, weights):
    while start <= end:
        mid = (start + end) // 2
        if weights[mid] == c:
            return mid
        if weights[mid] < c:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def event(n, c, weights):
    if binarySearch(0, n - 1, c, weights) >= 0:# 고른 물건 1개
        return True
    i = 0
    j = n - 1
    while(i < j): # 고른 물건 2개 or 3개
        weightSum = weights[i] + weights[j]
        if weightSum > c:
            j -= 1
        elif weightSum == c: # 고른 물건 2개
            return True
        else:
            diff = c- weightSum
            if diff != weights[i] and diff != weights[j] and binarySearch(0, n - 1, diff, weights) >= 0:
                return True # 고른 물건 3개
            i += 1
    return False

# N : 물건 개수, C : 무게
input = sys.stdin.readline
N, C = map(int, input().split(" "))

# N개의 물건의 무게들
weights = list(map(int, input().split(" ")))
weights.sort()

if event(N, C, weights):
    print(1)
else:
    print(0)