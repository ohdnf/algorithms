import sys
sys.stdin = open('input.txt')

def dfs(n, V, t):
    if n == t:
        return 1
    else:
        visited[n] = 1
        for k in range(1, V+1):
            if adj[n][k] and not visited[k]:
                if dfs(k, V, t):
                    return 1
        return 0

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    result = 0
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u][v] = 1
    start, goal = map(int, input().split())
    result = dfs(start, V, goal)
    print('#{} {}'.format(test_case, result))
