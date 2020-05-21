import sys
sys.stdin = open('input.txt')

def dfs(idx, last, cost):
    global min_cost
    if idx == last:
        if min_cost > cost:
            min_cost = cost
    elif min_cost < cost:
        return
    else:
        for factory in range(N):
            if not used[factory]:
                used[factory] = True
                dfs(idx+1, last, cost+prod_cost[idx][factory])
                used[factory] = False

t = int(input())
for test_case in range(1, t+1):
    N = int(input())
    prod_cost = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * N
    min_cost = N * 100
    dfs(0, N, 0)
    print('#{} {}'.format(test_case, min_cost))