import sys
sys.stdin = open('input.txt')
# sys.stdin = open('swea/mock_exam/1861/input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def wander(start, n, x, y, room, move):
    global max_move, max_start
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >= 0 and nx < n and ny >= 0 and ny < n and matrix[nx][ny] - 1 == room:
            wander(start, n, nx, ny, matrix[nx][ny], move+1)
            break
    else:
        if move > max_move:
            result.append([start, move])

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = list()
    max_start = n**2
    max_move = 0
    for i in range(n):
        for j in range(n):
            wander(matrix[i][j], n, i, j, matrix[i][j], 1)
    result.sort(key=lambda r: (-r[1], r[0]))
    room_number, max_moves = result[0]
    print('#{} {} {}'.format(test_case, room_number, max_moves))