import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    e, n = map(int, input().split())
    edges = list(map(int, input().split()))
    adj = [list() for _ in range(e+2)]
    for idx in range(0, e*2, 2):
        parent = edges[idx]
        child = edges[idx+1]
        adj[parent].append(child)
    q = [n,]
    result = 0
    while q:
        curr = q.pop(0)
        result += 1
        for node in adj[curr]:
            q.append(node)
    print('#{} {}'.format(test_case, result))
    