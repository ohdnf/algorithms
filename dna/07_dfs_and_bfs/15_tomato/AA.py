from collections import deque as dq
import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 안 익은 토마토 검사
def count_green():
    green = 0
    for row in range(N):
        for col in range(M):
            if box[row][col] == 0:
                green += 1
    return green

# 0일째 익은 토마토 검사
ripen = dq()
for row in range(N):
    for col in range(M):
        if box[row][col] == 1:
            # chk[row][col] = True
            ripen.append((row, col))

d = ((0,1),(1,0),(0,-1),(-1,0))
day = 0

green = count_green()

# 1일째부터 토마토 익을 때까지 검사
while green:
    for _ in range(len(ripen)):
        row, col = ripen.popleft()
        for drow, dcol in d:
            nrow, ncol = row+drow, col+dcol
            if 0<=nrow<N and 0<=ncol<M and box[nrow][ncol] == 0:
                box[nrow][ncol] = 1
                ripen.append((nrow, ncol))
    left = count_green()
    if green == left:
        day = -1
        break
    else:
        green = left
    day += 1
    # for tomatoes in box:
    #     print(tomatoes)
    # print()

print(day)