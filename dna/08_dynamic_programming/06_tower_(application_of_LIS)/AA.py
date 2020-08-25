import sys
# sys.stdin = open('in5.txt')

n = int(input())
brick = [tuple(map(int, input().split())) for _ in range(n)]     # 벽돌 밑면의 넓이, 벽돌의 높이, 벽돌의 무게

brick.sort(key=lambda b: (-b[0], -b[2], -b[1]))

tower = [0] * n
for i in range(len(brick)): # i = 벽돌의 번호(0 ~ n-1)
    tower[i] = brick[i][1]
    for j in range(i):   # j = i번째 벽돌이 제일 위에 있는 경우
        if brick[j][2] > brick[i][2] and (tower[j] + brick[i][1]) > tower[i]:
            tower[i] = tower[j] + brick[i][1]

print(max(tower))
