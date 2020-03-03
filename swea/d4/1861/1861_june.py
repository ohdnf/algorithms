import sys
sys.stdin = open('input.txt')
sys.stdin = open('n1000.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    v = [0] * (n**2 + 1)
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n and room[i][j] + 1 == room[nx][ny]:
                    v[room[i][j]] += 1
                    break
    start = 0
    move = max_move = 1
    for i in range(n*n, -1, -1):
        if v[i]:
            move += 1
        else:
            if move >= max_move:
                max_move = move
                start = i+1
            move = 1
    print('#{} {} {}'.format(test_case, start, max_move))
