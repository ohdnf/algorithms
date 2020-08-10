import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
adj = {node: [] for node in range(n+1)}
visited = [False]*(n+1)
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)

arrived = 0

def dfs(node):
    global arrived
    if node == n:
        arrived += 1
    else:
        visited[node] = True
        for nxt in adj[node]:
            if not visited[nxt]:
                dfs(nxt)
        visited[node] = False

dfs(1)

print(arrived)


