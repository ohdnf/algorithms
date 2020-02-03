import queue
import sys

input = lambda: sys.stdin.readline().rstrip()

n, m, v = map(int, input().split())
edges = []
for _ in range(m):
    n1, n2 = map(int, input().split())
    edges.append((n1, n2))

# DFS
# 첫 정점에서 갈 수 있는 정점
q = queue.Queue()



# BFS
queue = []
bfs = []