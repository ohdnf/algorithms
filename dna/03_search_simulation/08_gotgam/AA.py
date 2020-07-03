import sys
from collections import deque
input = lambda: sys.stdin.readline()

# for tc in range(1, 6):
#     sys.stdin = open(f'in{tc}.txt')
#     # sys.stdin = open(f'dna/03_search_simulation/08_gotgam/in{tc}.txt')

n = int(input())
gam = [deque(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    r, d, t = map(int, input().split()) # row, direction, times
    if not d:
        t = -t
    gam[r-1].rotate(t)

center = i = n // 2
res = 0
for j in range(n):
    tmp = list(gam[j])
    res += sum(tmp[center-i:center+i+1])
    if j < center:
        i -= 1
    else:
        i += 1
print(res)
