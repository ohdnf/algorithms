# 인접행렬(가중치 방향그래프)

"""
입력
6 9
1 2 7
1 3 4
2 1 2
2 3 5
2 5 5
3 4 5
4 2 2
4 5 5
6 4 5

출력
0 7 4 0 0 0
2 0 5 0 5 0
0 0 0 5 0 0
0 2 0 0 5 0
0 0 0 0 0 0
0 0 0 5 0 0
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
adj = [[0]*n for _ in range(n)]
for _ in range(m):
    s, e, w = map(int, input().split())
    adj[s-1][e-1] = w

for line in adj:
    print(*line)
