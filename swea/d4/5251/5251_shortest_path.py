import sys
from collections import deque
sys.stdin = open('input.txt')

t = int(input())

for test_case in range(1, t+1):
    N, E = map(int, input().split())
    adj = { node: list() for node in range(N+1) }
    for _ in range(E):
        s, e, w = map(int, input().split()) # 시작정점, 끝정점, 거리
        adj[s].append((e, w))
    
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[0] = 0
    q = deque([(0, 0)])
    
    while q:
        cur, d = q.popleft()    # 현재 정점, 0번 정점부터 거리
        for nxt, cost in adj[cur]:
            if dist[nxt] > d + cost:
                dist[nxt] = d + cost
                q.append((nxt, dist[nxt]))
        
    print('#{} {}'.format(test_case, dist[N]))
