from collections import deque
import sys
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
w = deque(sorted(list(map(int, input().split()))))

res = 0
while w:
    mx = w.pop()
    res += 1
    if not w:
        break
    if m - mx >= w[0]:
        w.popleft()
print(res)