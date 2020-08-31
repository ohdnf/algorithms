from collections import deque as dq
import sys
input = lambda: sys.stdin.readline().rstrip()

sys.stdin = open('input.txt')

"""
6 6
1 4
5 4
4 3
2 5
2 3
6 2

1 6 2 5 4 3
"""

n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
degree = [0]*n
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1
    degree[v-1] += 1

q = dq()
for i in range(n):
    if degree[i] == 0:
        q.append(i)

order = list()

while q:
    node = q.popleft()
    order.append(node+1)
    for nxt in range(n):
        if graph[node][nxt]:
            degree[nxt] -= 1
            if degree[nxt] == 0:
                q.append(nxt)

print(*order)



"""
n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
degree = [0]*n
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1
    degree[v-1] += 1

q = dq()

for v in range(n):
    for u in range(n):
        if graph[u][v]:
            break
    else:
        q.append(v)

done = [False] * n

order = list()

while q:
    node = q.popleft()
    # print(node)
    order.append(node+1)
    done[node] = True
    for v in range(n):
        if not done[v] and graph[node][v]:
            graph[node][v] = 0
            for u in range(n):
                if graph[u][v]:
                    break
            else:
                q.append(v)

print(*order)
"""