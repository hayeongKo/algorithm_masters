import sys

input = sys.stdin.readline
N = int(input())

def convert_to_seconds(time):
    minutes, seconds = map(int, time.split(":"))
    return minutes * 60 + seconds

def convert_to_mmss(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def substract_times(time1, time2):
    second1 = convert_to_seconds(time1)
    second2 = convert_to_seconds(time2)
    return second2 - second1

score1 = 0
score2 = 0
time1 = 0
time2 = 0
prev = "00:00"

goal_teams = []
win_times = []
prev = 0

for i in range(N):
    team, time = map(str, input().split(" "))
    goal_teams.append(team)
    if i == 0:
        prev = time
    else:
        win_times.append(substract_times(prev, time))
        prev = time
        if i == N-1:
            win_times.append(substract_times(time, "48:00"))

if N == 1:
    if goal_teams[0] == "1":
        print(convert_to_mmss(substract_times(time, "48:00")))
        print("00:00")
    else:
        print("00:00")
        print(convert_to_mmss(substract_times(time, "48:00")))
else:
    for i in range(N):
        if goal_teams[i] == "1":
            score1 += 1
        else:
            score2 += 1

        if score1 > score2:
            time1 += win_times[i]
        elif score1 < score2:
            time2 += win_times[i]

    print(convert_to_mmss(time1))
    print(convert_to_mmss(time2))