import sys
sys.stdin = open('input.txt')

def check_brick(x, y):
    global w, h
    number = bricks[x][y]
    to_be_destroyed[x][y] = True
    if number > 1:
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            for dist in range(1, number):
                nx = x + dx*dist
                ny = y + dy*dist
                if 0<=nx<h and 0<=ny<w and not to_be_destroyed[nx][ny]:
                    if bricks[nx][ny] > 1:
                        check_brick(nx, ny)
                    elif bricks[nx][ny] == 1:
                        to_be_destroyed[nx][ny] = True
                    elif bricks[nx][ny] == 0:
                        break

t = int(input())
for test_case in range(1, t+1):
    n, h, w = map(int, input().split()) # swap w, h to use zip()
    data = [list(map(int, input().split())) for _ in range(w)]
    bricks = [list(line) for line in list(zip(*data))]
    
    top = list()
    for row in range(h):
        for col in range(w):
            if bricks[row][col]:
                top.append((row, col))
                break
    x, y = top.pop()
    to_be_destroyed = [[False for _ in range(w)] for _ in range(h)]
    check_brick(x, y)
    # check된 벽돌 없애고
    # 없앤 자리 채우기
    print('#{}'.format(test_case))
