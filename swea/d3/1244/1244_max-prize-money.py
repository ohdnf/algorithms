import sys
sys.stdin = open('input.txt')

MAXSIZE = 720    # 6! = 720

def swap(prize, i, j):
    arr = [0] * digits
    for i in range(digits-1, -1, -1):
        arr[i] = prize % 10
        prize //= 10
    
    arr[i], arr[j] = arr[j], arr[i]

    res = 0
    for i in range(digits):
        res = res*10 + arr[i]

    return res

def dfs(prize, final, stage):
    global result

    for i in range(MAXSIZE):
        if memo[stage][i] == 0:
            memo[stage][i] = prize
            break
        elif memo[stage][i] == prize:
            return

    if stage == final:
        if prize > result: result = prize
    else:
        for i in range(digits-1):
            for j in range(i+1, digits):
                dfs(swap(prize, i, j), final, stage+1)


t = int(input())

for case in range(1, t+1):
    money, chance = map(int, input().split())
    memo = [[0]*MAXSIZE for _ in range(chance+1)]

    digits = len(str(money))
    result = 0

    dfs(money, chance, 0)
        
    print('#{} {}'.format(case, result))