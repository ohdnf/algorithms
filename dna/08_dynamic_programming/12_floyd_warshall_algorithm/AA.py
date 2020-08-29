import sys
# sys.stdin = open('in1.txt')

n, m = map(int, input().split())
dist = [[float('inf')]*n for _ in range(n)] # 가중치를 무한대로 초기화

# 자기 자신으로 가는 가중치는 0
for l in range(n):
    dist[l][l] = 0

# (s에서 e로 바로 가는) 간선의 가중치 적용
for _ in range(m):
    s, e, w = map(int, input().split())
    dist[s-1][e-1] = w

# k 정점을 경유하는 경로 갱신
for k in range(n):
    for i in range(n):
        if i != k:
            for j in range(n):
                if j != i and j != k:
                    dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j])

for line in dist:
    for v in line:
        if v == float('inf'):
            print('M', end=' ')
        else:
            print(v, end=' ')
    print()
