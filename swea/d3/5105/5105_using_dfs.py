import sys
sys.stdin = open('input.txt')

def bfs(x, y, move):
    global min_move, n
    if maze[x][y] == '3':
        if min_move > move:
            min_move = move - 1
    elif min_move < move:
        return
    else:
        visited[x][y] = True
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if maze[nx][ny] != '1':
                    bfs(nx, ny, move+1)

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    # 0:aisle 1:wall 2:start 3:goal
    # Find start
    x = y = -1
    for row in range(n):
        for col in range(n):
            if maze[row][col] == '2':
                x = row
                y = col
                break
        if x != -1:
            break
    min_move = n*n
    bfs(x, y, 0)
    if min_move == n*n:
        min_move = 0
    print('#{} {}'.format(test_case, min_move))