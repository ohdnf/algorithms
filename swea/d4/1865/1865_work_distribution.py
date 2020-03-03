import sys
sys.stdin = open('input.txt')

def dfs(worker, total, percent):
    global max_percent
    if worker == total:
        if max_percent < percent:
            max_percent = percent
    elif percent <= max_percent:
        return
    else:
        for job in range(total):
            if not done[job]:
                done[job] = True
                dfs(worker+1, total, percent*(productivity[worker][job]/100))
                done[job] = False

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    productivity = [list(map(int, input().split())) for _ in range(n)]
    max_percent = 0
    done = [False] * n
    dfs(0, n, 1)
    print('#{0} {1:.6f}'.format(test_case, round(max_percent*100, 6)))