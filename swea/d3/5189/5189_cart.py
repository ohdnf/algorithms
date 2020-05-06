import sys
sys.stdin = open('input.txt')

def dfs(curr_len, total_len, curr, total):
    global min_usage
    if curr_len == total_len-1:
        total += cost[curr][0]
        min_usage = min(total, min_usage)
    elif min_usage <= total:
        return
    else:
        for nxt in range(total_len):
            if not visited[nxt]:
                visited[nxt] = True
                dfs(curr_len+1, total_len, nxt, total+cost[curr][nxt])
                visited[nxt] = False

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    min_usage = 100*n
    visited = [False]*n
    visited[0] = True
    dfs(0, n, 0, 0)
    print('#{} {}'.format(test_case, min_usage))