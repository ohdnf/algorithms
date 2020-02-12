import sys
sys.stdin = open('input.txt')

def check_hrz(sudoku):
    for line in sudoku:
        if len(set(line)) != 9:
            return False
    return True

def check_vrt(sudoku):
    sudoku = list(zip(*sudoku))
    return check_hrz(sudoku)

def check_box(sudoku):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [sudoku[i+row][j+col] for col in range(3) for row in range(3)]
            if len(set(box)) != 9:
                return False
    return True

T = int(input())
for t in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    if not check_hrz(sudoku):
        result = 0
    else:
        if not check_vrt(sudoku):
            result = 0
        else:
            if not check_box(sudoku):
                result = 0
    print('#{0} {1}'.format(t, result))