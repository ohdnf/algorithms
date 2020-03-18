import sys
sys.stdin = open('input.txt')

def remove(col, mar, w, h, bricks):
    q = list()
    row = 0
    while row < h and bricks[row][col] == 0:    # 맨 위 벽돌 찾기
        row += 1
    if row == h:    # 벽돌이 없는 경우
        return
    q.append((row, col))
    while q:
        x, y = q.pop(0)
        number = bricks[x][y]   # 벽돌 숫자
        bricks[x][y] = 0
        for dist in range(1, number):
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx = x + dx*dist
                ny = y + dy*dist
                if 0<=nx<h and 0<=ny<w:
                    q.append((nx, ny))

def shoot(mar, w, h):
    bricks = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            bricks[i][j] = org[i][j]
    for i in range(mar):
        remove(p[i], mar, w, h, bricks)
        # 아래로 떨굴 벽돌 찾기
        for j in range(w):
            for k in range(h-1, 0, -1):
                q = k
                while q > 1 and bricks[q][j] == 0:
                    q -= 1
                if q != k:
                    bricks[k][j] = bricks[q][j]
                    bricks[q][j] = 0
    # 남은 벽돌 세기
    cnt = 0
    for i in range(h):
        for j in range(w):
            if bricks[i][j] != 0:
                cnt += 1
    return cnt

def npr(marble, last, w, h):
    global min_value
    if marble == last:
        res = shoot(marble, w, h)   # 남은 벽돌을 리턴
        if min_value > res:
            min_value = res
    else:
        for i in range(w):
            p[marble] = i
            npr(marble+1, last, w, h)
            if min_value == 0:
                return
    

t = int(input())
for test_case in range(1, t+1):
    n, w, h = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(h)]   # 초기 벽돌
    p = [0] * n     # N번 구슬을 쏠 가로 위치
    min_value = w*h
    npr(0, n, w, h)
    print('#{} {}'.format(test_case, min_value))
    