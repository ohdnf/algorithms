import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(1, 11):
    test_case = int(input())
    maze = [list(input()) for _ in range(16)]
    stack = []
    # 1: wall / 2: start / 3: finish

    x = y = -1
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                x, y = i, j
                break
    
    possible = True
    finish = False
    if x == -1:
        possible = False
    else:
        stack.append((x, y))
    
    while stack and not finish:
        x, y = stack.pop()
        maze[x][y] = '1'
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 16 and ny < 16 and nx > -1 and ny > -1:
                if maze[nx][ny] == '3':
                    finish = True
                    break
                elif maze[nx][ny] == '0':
                    stack.append((nx, ny))

    result = 0
    if possible and finish:
        result = 1
    print('#{} {}'.format(test_case, result))