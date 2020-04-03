import sys
# sys.stdin = open('input.txt')
sys.stdin = open('input2.txt')

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    # 0:aisle 1:wall 2:start 3:goal

    # Find start
    q = list()
    for row in range(n):
        for col in range(n):
            if maze[row][col] == '2':
                q.append((row, col))
                break
        if q:
            break
    
    min_move = 0
    # BFS
    while q:
        if min_move:
            break
        x, y = q.pop(0)
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if maze[nx][ny] == '3':     # Goal
                    # if min_move > visited[x][y]:
                    #     min_move = visited[x][y]
                    min_move = visited[x][y]
                    break
                elif maze[nx][ny] != '1':   # Go ahead
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    # if min_move == n*n:
    #     min_move = 0    # Cannot reach the goal
    print('#{} {}'.format(test_case, min_move))