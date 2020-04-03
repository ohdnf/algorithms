import sys
sys.stdin = open('input.txt')

def distance(node, goal, move):
    global min_dist
    global connected
    if node == goal:
        if move < min_dist:
            min_dist = move
        connected = True
    elif move >= min_dist:
        return
    else:
        visited[node] = True
        for nxt in graph[node]:
            if not visited[nxt]:
                distance(nxt, goal, move+1)
        visited[node] = False

t = int(input())
for test_case in range(1, t+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # undirected graph
    start, goal = map(int, input().split())
    min_dist = e
    connected = False
    distance(start, goal, 0)
    if not connected:
        min_dist = 0
    print('#{} {}'.format(test_case, min_dist))