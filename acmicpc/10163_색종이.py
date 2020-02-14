import sys
input = lambda: sys.stdin.readline()

blank = [[0 for _ in range(102)] for _ in range(102)]

n = int(input())
for i in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for r in range(x, x+w):
        for c in range(y, y+h):
            blank[r][c] = i

for i in range(1, n+1):
    cnt = 0
    for line in blank:
        cnt += line.count(i)
    print(cnt)