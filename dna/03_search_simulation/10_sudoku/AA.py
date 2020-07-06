sudoku = [list(map(int, input().split())) for _ in range(9)]
rev = list(zip(*sudoku))
isSudoku = 'YES'

# row and col
for i in range(9):
    row = len(set(sudoku[i]))
    col = len(set(rev[i]))
    if row != 9 or col != 9:
        isSudoku = 'NO'
        break

if isSudoku == 'YES':
    # square
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = set([sudoku[x][y] for x in range(i, i+3) for y in range(j, j+3)])
            if len(tmp) != 9:
                isSudoku = 'NO'
                break
        if isSudoku == 'NO':
            break

print(isSudoku)