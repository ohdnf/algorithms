import sys
sys.stdin = open('input.txt')

# 동, 서, 남, 북
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(n)]

    max_pang = 0
    for row in range(n):
        for col in range(m):
            pang = balloons[row][col]
            for move in range(4):
                cnt = balloons[row][col]
                nr, nc = row, col
                v, h = dr[move], dc[move]
                while cnt:
                    nr += v
                    nc += h
                    cnt -= 1
                    if nr < 0 or nr >= n or nc < 0 or nc >= m:
                        break
                    pang += balloons[nr][nc]
            if pang > max_pang:
                max_pang = pang
    
    print('#{0} {1}'.format(t, max_pang))