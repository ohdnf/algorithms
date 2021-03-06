import sys
sys.stdin = open('input.txt')

def shoot(shots, bricks):
    global w, h
    q = list()
    for row in top:
        # 맨 위 벽돌 선택
        for col in range(w):
            if bricks[row][col]:
                q.append((row, col))
                break
        else:
            return
        # ㄹㅇ 벽돌 깨기
        while q:
            x, y = q.pop(0)
            number = bricks[x][y]
            bricks[x][y] = 0
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                for dist in range(1, number):
                    nx = x + dx*dist
                    ny = y + dy*dist
                    if 0<=nx<h and 0<=ny<w and bricks[nx][ny]:
                        q.append((nx, ny))
        # 벽돌 정리
        for row in range(h):
            for col in range(w):
                if bricks[row][col] == 0:
                    bricks[row] = [bricks[row].pop(col)] + bricks[row]

def dfs(shot, last):
    global w, h, min_bricks
    if shot == last:
        # 벽돌 복사
        bricks = [[0]*w for _ in range(h)]
        for row in range(h):
            for col in range(w):
                bricks[row][col] = orig[row][col]
        # 벽돌 깨기
        shoot(last, bricks)
        # 남은 벽돌 세기
        rest = 0
        for line in bricks:
            rest += w - line.count(0)
        if min_bricks > rest:
            min_bricks = rest
    elif min_bricks == 0:
        return
    else:
        for row in range(h):
            top[shot] = row
            dfs(shot+1, last)

t = int(input())
for test_case in range(1, t+1):
    n, h, w = map(int, input().split()) # swap w, h to use zip()
    data = [list(map(int, input().split())) for _ in range(w)]
    orig = [list(line) for line in list(zip(*data))]
    min_bricks = h * w
    top = [0] * n
    dfs(0, n)
    print('#{} {}'.format(test_case, min_bricks))
