import queue
import sys
input = lambda: sys.stdin.readline().rstrip()

# 정점의 개수, 간선의 개수, 시작 정점
n, m, v = map(int, input().split())

edges = [list() for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    # 양방향 그래프
    # edges[x][y] = edges[y][x] = 1
    edges[x].append(y)
    edges[y].append(x)

# 정점 번호가 작은 순으로 탐색 ==> 오름차순으로 정렬
# for edge in edges:
#     edge.sort()
edges = [sorted(edge) for edge in edges]


# BFS
visited = [False]*(n+1)  # 중복 방문 방지
res_bfs = []
def bfs(start):
    q = queue.Queue()
    q.put(start)
    visited[start] = True
    while not q.empty():
        current = q.get()               # First out
        res_bfs.append(current)         # Visit order
        for node in edges[current]:     # Visit current node's edges
            if not visited[node]:       # Check each node in edges
                visited[node] = True    # Check if visited
                q.put(node)             # Last in
    return

bfs(v)

# DFS
visited = [False]*(n+1)
res_dfs = []

def dfs(node):
    visited[node] = True            # 노드 방문
    res_dfs.append(node)            # 방문 순서
    for nxt in edges[node]:         # 인접 노드 순회
        if not visited[nxt]:        # 방문하지 않는 노드
            dfs(nxt)                # 방문 ㄱㄱ
    return

dfs(v)

for res in (res_dfs, res_bfs):
    print(' '.join(map(str, res)))
