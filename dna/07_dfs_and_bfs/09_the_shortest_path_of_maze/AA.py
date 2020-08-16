from collections import deque as dq
import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')

maze = [list(map(int, input().split())) for _ in range(7)]
visited = [[0] * 7 for _ in range(7)]
search = dq()
search.append((0, 0, 0))
visited[0][0] = 1

d = ((0, 1), (0, -1), (1, 0), (-1, 0))

res = 0
min_move = 49
while search:
    row, col, move = search.popleft()
    if row == 6 and col == 6:
        res = 1
        if min_move > move:
            min_move = move
    else:
        for drow, dcol in d:
            nrow, ncol = row+drow, col+dcol
            if 0<=nrow<7 and 0<=ncol<7 and not visited[nrow][ncol] and maze[nrow][ncol] == 0:
                visited[nrow][ncol] = 1
                search.append((nrow, ncol, move+1))
    
    # for line in visited:
    #     print(line)
    # print()

if res:
    print(min_move)
else:
    print(-1)