import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')

ladder = [list(map(int, input().split())) for _ in range(10)]

d = ((0, -1), (0, 1), (-1, 0))
res = start = -1
for scol in range(10):
    if ladder[9][scol] == 2:
        start = scol
        break

def find(row, col):
    global res
    if row == 0:
        res = col
    else:
        ladder[row][col] = 0
        side = False
        for drow, dcol in d:
            nrow, ncol = row+drow, col+dcol
            if 0<=nrow<10 and 0<=ncol<10 and ladder[nrow][ncol]:
                if drow == 0 and (dcol == -1 or dcol == 1):
                    side = True
                if drow == -1 and dcol == 0 and side:
                    break
                find(nrow, ncol)

find(9, start)

print(res)