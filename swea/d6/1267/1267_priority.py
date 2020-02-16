import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))
    # graph = [[] for _ in range(v+1)]
    required = [[] for _ in range(v+1)]
    finished = [False for _ in range(v+1)]
    finished[0] = True
    for i in range(0, e*2, 2):
        f, t = edges[i], edges[i+1]
        # graph[f].append(t)
        required[t].append(f)

    orders = []
    curr = 1
    while not all(finished):
        if finished[curr]:
            pass
        else:
            if not required[curr]:
                finished[curr] = True
                orders.append(curr)
            else:
                tmp = [finished[check] for check in required[curr]]
                if all(tmp):
                    finished[curr] = True
                    orders.append(curr)
        curr += 1
        if curr > v:
            curr = 1
    
    print('#{}'.format(test_case), end=' ')
    print(*orders)