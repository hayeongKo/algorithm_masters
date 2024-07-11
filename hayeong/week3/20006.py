import sys

input = sys.stdin.readline
p, m = map(int, input().split(" "))

players = []
waiting_room = [[] for i in range(300)]
compacted = [False for i in range(300)]
ranges = [[] for i in range(300)]

def insert_waitingroom(level, name):
    for j in range(len(ranges)):
        # level 조건이랑 빈자리 없다보면 결국 비어있는 ranges까지 넘어오게 될 것 
        # 이때 새로운 방 파기
        if ranges[j] == []:
            ranges[j] = [int(level)-10, int(level)+10]
            waiting_room[j].append([level, name])
            return
        # level 조건 성립하고, 방에 빈 자리가 있을때
        elif int(level) in range(ranges[j][0], ranges[j][1]+1) and compacted[j] == False:
            waiting_room[j].append([level, name])
            if len(waiting_room[j]) == m:
                compacted[j] = True
            return
        # 조건 성립 안하면 일단 넘겨
        else:
            continue

for i in range(p):
    level, name = map(str, input().rstrip().split())
    if i == 0:
        waiting_room[0].append([level, name])
        ranges[0] = [int(level)-10, int(level)+10]
    else:
        if m == 1:
            waiting_room[i].append([level, name])
        else:
            insert_waitingroom(level, name)

# 출력
for room in waiting_room:
    if len(room) == m:
        print("Started!")
    else:
        if len(room) == 0:
            break
        print("Waiting!")
    room.sort(key = lambda x : (x[1]))
    for player in room:
        print("{0} {1}".format(player[0], player[1]))

