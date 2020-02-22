import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(10):
    test_case = int(input())
    maze = [list(input()) for _ in range(100)]
    stack = list()
    # 0: path / 1: wall / 2: start / 3: end
    x = y = -1
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                x, y = i, j
                stack.append((x, y))
                break
        if x != -1:
            break
    
    finish = 0
    
    while stack and not finish:
        x, y = stack.pop()
        maze[x][y] = '1'
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx > -1 and nx < 100 and ny > -1 and ny < 100:
                if maze[nx][ny] == '3':
                    finish = 1
                    break
                elif maze[nx][ny] == '0':
                    stack.append((nx, ny))
    
    print('#{} {}'.format(test_case, finish))