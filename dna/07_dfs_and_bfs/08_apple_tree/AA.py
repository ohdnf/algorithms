from collections import deque as dq
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
mid = n // 2
coord = dq()
coord.append((mid, mid, 0))
apples = tree[mid][mid]
visited[mid][mid] = True
d = ((0, 1), (0, -1), (-1, 0), (1, 0))
while coord:
    row, col, move = coord.popleft()
    if move < mid:
        for dr, dc in d:
            nr, nc = row+dr, col+dc
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                visited[nr][nc] = True
                apples += tree[nr][nc]
                coord.append((nr, nc, move+1))

print(apples)