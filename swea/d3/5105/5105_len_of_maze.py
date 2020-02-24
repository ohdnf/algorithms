# queue 써서 다시 풀기...T^T

import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 0:path / 1:wall / 2:start / 3:goal
def search(r, c, goal, move):
    global min_move
    global finish
    if maze[r][c] == goal:
        if move < min_move:
            min_move = move - 1
        finish = True
    elif move >= min_move:
        return
    else:
        maze[r][c] = '1'
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                if maze[nr][nc] != '1':
                    search(nr, nc, goal, move+1)

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    # visited = [[False for _ in range(n)] for _ in range(n)]
    x = y = -1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                x, y = i, j
                break
        if x != -1:
            break
    min_move = n**2
    finish = False
    search(x, y, '3', 0)
    if not finish:
        min_move = 0
    print('#{} {}'.format(test_case, min_move))