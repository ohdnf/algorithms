import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
# 아래 주사위의 윗면에 적힌 숫자, 한 옆면 숫자의 합
sides = [[i+1, 0] for i in range(6)]
for _ in range(n):
    dice = list(map(int, input().split()))
    temp = []
    for i in range(6):
        bottom = dice[i]
        if i == 0 or i == 5:
            j = -(i+1)
        elif i in (1, 2):
            j = i + 2
        elif i in (3, 4):
            j = i - 2
        top = dice[j]
        for k in range(6):
            if bottom == sides[k][0]:
                side = list(range(1, 7))
                side.remove(bottom)
                side.remove(top)
                temp.append([top, sides[k][1] + max(side)])
                break
    sides = temp
result = max(sides, key=lambda s: s[1])
print(result[1])