import sys

input = sys.stdin.readline

N = int(input())
nums_bigger = [[] for _ in range(N)]
answers = []

i = 1
for bigger_num in list(map(int, input().split(" "))):
    nums_bigger[bigger_num].append(i)
    i += 1

def update_status_bigger():
    status_bigger = [0] * N
    for i in range(N):
        for answer in answers:
            if len(nums_bigger[i]) != 0:
                if nums_bigger[i][0] < answer:
                    status_bigger[i] += 1
    return status_bigger

def insert_answers(status_bigger):
    same_status = []
    for i in range(len(status_bigger)):
        if len(nums_bigger[i]) != 0 and i == status_bigger[i]:
            same_status.append([nums_bigger[i][0], i])
    answers.append(nums_bigger[sorted(same_status)[0][1]].pop(0))


answers.append(nums_bigger[0].pop(0)) # 처음 시작엔 본인보다 키 큰 사람이 왼쪽에 0번인 사람의 첫번째 요소

while len(answers) != N:
    status_bigger = update_status_bigger()
    if insert_answers(status_bigger):
        continue
    
print(*(answers))
