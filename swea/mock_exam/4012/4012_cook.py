import sys
sys.stdin = open('input.txt')

def dfs(length, half, number, last):
    if length == half:
        ingr_a = [num for num in range(n) if check[num]]
        ingr_b = [num for num in range(n) if not check[num]]
        s_a = s_b = 0
        for i in ingr_a:
            for j in ingr_a:
                s_a += synergy[i][j]
        for i in ingr_b:
            for j in ingr_b:
                s_b += synergy[i][j]
        result.append(abs(s_a - s_b))
    elif number == last:
        return
    else:
        check[number] = True
        dfs(length+1, half, number+1, last)
        check[number] = False
        dfs(length, half, number+1, last)

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]
    check = [False for _ in range(n)]
    groceries = list(range(n))
    result = list()
    dfs(0, int(n/2), 0, n)
    print('#{} {}'.format(test_case, min(result)))