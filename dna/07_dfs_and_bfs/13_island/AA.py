from collections import deque as dq
import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False]*n for _ in range(n)]
# 방문한 곳을 0으로 바꾸기

d = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
islands = 0

for row in range(n):
    for col in range(n):
        # if grid[row][col] and not visited[row][col]:
        if grid[row][col]:
            search = dq()
            search.append((row, col))
            grid[row][col] = 0
            # visited[row][col] = True
            while search:
                crow, ccol = search.popleft()
                for drow, dcol in d:
                    nrow, ncol = crow+drow, ccol+dcol
                    # if 0<=nrow<n and 0<=ncol<n and grid[nrow][ncol] and not visited[nrow][ncol]:
                    if 0<=nrow<n and 0<=ncol<n and grid[nrow][ncol]:
                        grid[nrow][ncol] = 0
                        search.append((nrow, ncol))
            islands += 1

print(islands)