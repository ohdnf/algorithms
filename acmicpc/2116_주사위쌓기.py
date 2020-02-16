# import sys
# input = lambda: sys.stdin.readline().rstrip()
# # 주사위 개수
# n = int(input())
# # (아래 주사위의 윗면에 적힌 숫자, 한 옆면 숫자의 합) * 6
# sides = [[i, 0] for i in range(1, 7)]
# for _ in range(n):
#     # A, B, C, D, E, F ==> A:F / B:D / C:E
#     dice = list(map(int, input().split()))
#     temp = []
#     for i in range(6):
#         bottom = dice[i]
#         if i == 0 or i == 5:
#             j = -(i+1)
#         elif i in (1, 2):
#             j = i+2
#         elif i in (3, 4):
#             j = i-2
#         top = dice[j]
#         for k in range(6):
#             if bottom == sides[k][0]:
#                 side = list(range(1, 7))
#                 side.remove(bottom)
#                 side.remove(top)
#                 temp.append([top, sides[k][1] + max(side)])
#                 break
#     sides = temp
# result = max(sides, key=lambda s: s[1])
# print(result[1])


import sys

opened_dice = [None, 6, 4, 5, 2, 3, 1]

def stacking(dice, c):
    c_idx = dice.index(c)
    nxt = dice[opened_dice[c_idx]]
    max_num = 0
    for i in dice[1:]:
        if i == c or i == nxt:
            continue
        if max_num < i:
            max_num = i

    return max_num, nxt


dices = []
for game in range(int(sys.stdin.readline())):
    dices.append([None] + list(map(int, sys.stdin.readline().split())))

result = 0
for i in range(1, 7):
    c = dices[0][i]
    max_num = 0
    for j in range(len(dices)):
        temp = stacking(dices[j], c)
        max_num += temp[0]
        c = temp[1]
    if result < max_num:
        result = max_num
print(result)

