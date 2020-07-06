import sys
input = lambda: sys.stdin.readline()

n = int(input())
mt = [list(map(int, input().split())) for _ in range(n)]

peaks = 0
for row in range(n):
    for col in range(n):
        curr = mt[row][col]
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = row + dx
            nc = col + dy
            if 0<=nr<n and 0<=nc<n and curr <= mt[nr][nc]:
                break
        else:
            peaks += 1

print(peaks)