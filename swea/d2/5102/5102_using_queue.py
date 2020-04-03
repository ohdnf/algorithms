import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    v, e = map(int, input().split())
    adj = [list() for _ in range(v+1)]
    visited = [0]*(v+1)
    for _ in range(e):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)
    s, g = map(int, input().split())
    q = list()
    q.append(s)
    min_move = v
    while q:
        curr = q.pop(0)
        for node in adj[curr]:
            if not visited[node]:
                if node == g:
                    if min_move > visited[curr]:
                        min_move = visited[curr] + 1
                        break
                else:
                    visited[node] = visited[curr] + 1
                    q.append(node)
    if min_move == v:
        min_move = 0
    print('#{} {}'.format(test_case, min_move))