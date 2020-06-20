import sys
sys.stdin = open('input.txt')

def make_set(node):
    p[node] = node

def find_set(node):
    if p[node] == node: return node
    else:
        p[node] = find_set(p[node])
        return p[node]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

t = int(input())

for test_case in range(1, t+1):
    V, E = map(int, input().split())    # 정점은 0 ~ V번 (총 V+1개)
    edges = [list(map(int, input().split())) for _ in range(E)]
    
    # 간선 가중치를 기준으로 정렬
    edges.sort(key=lambda w: w[2])

    p = [0] * (V+1)
    rank = [0] * (V+1)
    for node in range(V+1):
        make_set(node)
    
    # mst = list()
    cnt = 0     # 선택된 간선의 수
    weight = 0  # MST 간선 가중치의 합

    for i in range(E):
        n1, n2, w = edges[i]  # 시작 정점, 도착 정점, 가중치
        
        # 싸이클 검증
        if find_set(n1) == find_set(n2):  continue

        union(n1, n2)

        # mst.append(edges[i])
        weight += w
        cnt += 1

        # MST 완성 시 종료
        if cnt == V:  break

    print('#{} {}'.format(test_case, weight))