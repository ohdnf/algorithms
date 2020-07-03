import sys
input = lambda: sys.stdin.readline()

# sys.stdin = open('in1.txt')

n = int(input())
# players = list()
res = 0
for _ in range(n):
    # cnt = same_num = max_num = 0
    # numbers = sorted(list(map(int, input().split())))
    # for number in numbers:
    #     if number > max_num:
    #         max_num = number
    #     if number == same_num:
    #         cnt += 1
    #     else:
    #         same_num = number
    #         cnt = 1

    # if cnt == 3:
    #     players.append(10000 + same_num * 1000)
    # elif cnt == 2:
    #     players.append(1000 + same_num * 100)
    # else:
    #     players.append(max_num * 100)
    a, b, c = map(int, sorted(input().split()))
    if a==b and b==c:
        money = 10000 + a * 1000
    elif a==b or a==c:
        money = 1000 + a * 100
    elif b==c:
        money = 1000 + b * 100
    else:
        money = c * 100

    if res < money:
        res = money

# print(max(players))
print(res)