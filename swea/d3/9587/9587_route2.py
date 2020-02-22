import sys
sys.stdin = open('input.txt')


def dfs(node, total, target):
    if node == target:
        return 1
    else:
        visited[node] = 1
        for nxt in range(1, total+1):
            if adj[node][nxt] and not visited[nxt]:
                if dfs(nxt, total, target):
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
        adj[u][v] = 1   # Directed graph
    start, goal = map(int, input().split())
    result = dfs(start, V, goal)
    print('#{} {}'.format(test_case, result))
