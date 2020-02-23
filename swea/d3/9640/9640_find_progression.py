import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for test_case in range(1, T+1):
    n, *prog = input().split()
    n = int(n)
    m = int(input())
    matrix = [input().split() for _ in range(m)]
    starts = []
    x = y = -1
    for i in range(m):
        for j in range(m):
            if matrix[i][j] == prog[0]:
                starts.append((i, j))

    result = 0
    for start in starts:
        tmp = [line[:] for line in matrix]
        stack = [start]
        idx = 1
        while stack:
            x, y = stack.pop()
            tmp[x][y] = '0'
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and ny >= 0 and nx < m and ny < m:
                    if tmp[nx][ny] == prog[idx]:
                        if idx == n-1:
                            result = 1
                            break
                        else:
                            stack.append((nx, ny))
            idx += 1
            if idx == n:
                break
        if result:
            break
    print('#{} {}'.format(test_case, result))