import sys
input = lambda: sys.stdin.readline()

# sys.stdin = open('in1.txt')

n = int(input())
players = list()
for _ in range(n):
    cnt = same_num = max_num = 0
    numbers = sorted(list(map(int, input().split())))
    for number in numbers:
        if number > max_num:
            max_num = number
        if number == same_num:
            cnt += 1
        else:
            same_num = number
            cnt = 1

    if cnt == 3:
        players.append(10000 + same_num * 1000)
    elif cnt == 2:
        players.append(1000 + same_num * 100)
    else:
        players.append(max_num * 100)

print(max(players))