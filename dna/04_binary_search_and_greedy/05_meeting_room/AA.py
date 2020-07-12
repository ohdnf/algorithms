import sys
input = lambda: sys.stdin.readline()

n = int(input())
time_table = [list(map(int, input().split())) for _ in range(n)]

time_table.sort(key=lambda t: (t[1], t[0])) # 회의 종료시간을 기준으로 정렬

meetings = [time_table.pop(0),]

last_endtime = meetings[0][1]
for s, e in time_table:
    if s >= last_endtime:
        last_endtime = e
        meetings.append([s, e])

print(len(meetings))