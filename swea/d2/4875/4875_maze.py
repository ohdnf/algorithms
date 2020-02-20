import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, k):
    if maze[x][y] == k:
        return x, y
    else:
        for d in range(4):
            x += dx[d]
            y += dy[d]
            if x >= 0 and y >= 0 and x < n and y < n:
                if maze[x][y] == 0:
                    stack.append((x, y))

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    stack = list()
    result = '0'
    x, y = -1, -1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                x, y = i, j
                stack.append((x, y))
                break
    if x == -1:
        result = 'error'

    while stack:
        x, y = stack.pop()
        maze[x][y] = '1'
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if maze[nx][ny] == '3':
                    result = '1'
                    break
                elif maze[nx][ny] == '0':
                    stack.append((nx, ny))
    print('#{} {}'.format(test_case, result))