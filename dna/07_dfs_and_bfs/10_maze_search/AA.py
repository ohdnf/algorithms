import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')

maze = [list(map(int, input().split())) for _ in range(7)]
visited = [[False] * 7 for _ in range(7)]

d = ((0, 1), (1, 0), (0, -1), (-1, 0))
res = 0

def dfs(row, col):
    global res
    if row == 6 and col == 6:
        res += 1
    else:
        for drow, dcol in d:
            nrow, ncol = row+drow, col+dcol
            if 0<=nrow<7 and 0<=ncol<7 and not visited[nrow][ncol] and maze[nrow][ncol] != 1:
                visited[nrow][ncol] = True
                dfs(nrow, ncol)
                visited[nrow][ncol] = False
maze[0][0] = 1
dfs(0, 0)
print(res)