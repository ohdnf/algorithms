import sys
sys.stdin = open('input.txt')

def search(node, target):
    global result
    if node == target:
        result = 1
    else:
        visited[node] = True
        for nxt in directed[node]:
            if not visited[nxt]:
                search(nxt, target)

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    directed = [list() for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        directed[u].append(v)
    start, goal = map(int, input().split())
    visited = [False for _ in range(V+1)]
    result = 0
    search(start, goal)
    print('#{} {}'.format(test_case, result))
    