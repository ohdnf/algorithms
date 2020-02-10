import sys
input = lambda: sys.stdin.readline()

board = []
for _ in range(5):
    board.extend(list(map(int, input().split())))
incoming = []
for _ in range(5):
    incoming.extend(list(map(int, input().split())))
called = [[False for _ in range(5)] for _ in range(5)]
horizon = [False for _ in range(5)]
vertical = [False for _ in range(5)]
diagonal = [False, False]
bingo = 0
for i in range(25):
    now = incoming[i]
    loc = board.index(now)
    row = loc // 5
    col = loc % 5
    called[row][col] = True
    print()
    print(f'#{i+1}:{now}, row:{row}, col:{col}')
    for line in called:
        print(line)
    # 가로 확인
    if all(called[row]):
        if horizon[row]:
            pass
        else:
            bingo += 1
            horizon[row] = True
    if bingo == 3:
        print(i+1)
        break
    # 세로 확인
    if all([called[j][col] for j in range(5)]):
        if vertical[col]:
            pass
        else:
            bingo += 1
            vertical[col] = True
    if bingo == 3:
        print(i+1)
        break
    # 대각(우하향) 확인
    if row == col and all([called[j][j] for j in range(5)]):
        if diagonal[0]:
            pass
        else:
            bingo += 1
            diagonal[0] = True
    if bingo == 3:
        print(i+1)
        break
    # 대각(우상향) 확인
    if row == (4-col) and all([called[j][4-j] for j in range(5)]):
        if diagonal[1]:
            pass
        else:
            bingo += 1
            diagonal[1] = True
    if bingo == 3:
        print(i+1)
        break
