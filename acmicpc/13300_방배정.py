import sys
input = lambda: sys.stdin.readline()

n, k = map(int, input().split())
students = [[0 for _ in range(7)] for _ in range(2)]
for _ in range(n):
    s, y = map(int, input().split())
    students[s][y] += 1

rooms = 0
for s in range(2):
    for y in range(1, 7):
        cnt = students[s][y]
        rooms += cnt // k
        if cnt % k:
            rooms += 1

print(rooms)