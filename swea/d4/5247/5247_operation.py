import sys
sys.stdin = open('input.txt')

able = ['+1', '-1', '*2', '-10']
def dfs(number, target, trial):
    global result
    if number == target:
        if result > trial:
            result = trial
    elif trial > result:
        return
    else:
        for i in range(4):
            if i == 0:
                dfs(number*2, target, trial+1)
            elif i == 1:
                dfs(number-1, target, trial+1)
            elif i == 2:
                dfs(number+1, target, trial+1)
            elif i == 3:
                dfs(number-10, target, trial+1)

t = int(input())
for test_case in range(1, t+1):
    N, M = map(int, input().split())
    result = 1000000
    dfs(N, M, 0)

    print('#{} {}'.format(test_case, result))
