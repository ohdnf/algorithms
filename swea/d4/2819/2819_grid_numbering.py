import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, length, limit, number):
    if length == limit:
        result.add(number)
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<4 and 0<=ny<4:
                dfs(nx, ny, length+1, limit, number+grid[nx][ny])

t = int(input())
for test_case in range(1, t+1):
    grid = [input().split() for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, 7, grid[i][j])
    print('#{} {}'.format(test_case, len(result)))
