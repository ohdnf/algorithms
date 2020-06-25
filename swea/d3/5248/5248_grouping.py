import sys
sys.stdin = open('input.txt')

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x])
        return p[x]

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
    N, M = map(int, input().split())
    votes = list(map(int, input().split()))
    p = [0]*N
    rank = [0]*N
    for num in range(N):
        make_set(num)
    for i in range(0, 2*M, 2):
        union(votes[i]-1, votes[i+1]-1)
    parties = set()
    for student in range(N):
        parties.add(find_set(student))
    print('#{} {}'.format(test_case, len(parties)))