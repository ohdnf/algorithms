import sys
sys.stdin = open('input.txt')

directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    board = [ [0 for _ in range(n)] for _ in range(n) ]
    # 초기화
    center = n // 2
    for i in range(center-1, center+1):
        for j in range(center-1, center+1):
            if (i+j) % 2:
                board[i][j] = 1 # Black
            else:
                board[i][j] = 2 # White
    # 돌 놓기
    for _ in range(m):
        col, row, color = map(int, input().split())
        board[row-1][col-1] = color
        for d in directions:
            to_change = []
            curr_row, curr_col = row - 1 + d[0], col - 1 + d[1]
            while curr_row > -1 and curr_row < n and curr_col > -1 and curr_col < n:
                if board[curr_row][curr_col] == 0:
                    break
                elif board[curr_row][curr_col] == color:
                    for r, c in to_change:
                        board[r][c] = color
                    break
                else:
                    to_change.append([curr_row, curr_col])
                curr_row, curr_col = curr_row + d[0], curr_col + d[1]

    black, white = 0, 0
    for line in board:
        black += line.count(1)
        white += line.count(2)
    print('#{0} {1} {2}'.format(t, black, white))