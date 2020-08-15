from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

s, e = map(int, input().split())

find_calf = deque()
find_calf.append((s, 0))

res = float('inf')
while find_calf:
    curr, jump = find_calf.popleft()
    if curr == e:
        if res > jump:
            res = jump
    else:
        if curr < 1 or curr > 10000:
            continue
        elif curr > e:
            find_calf.append((curr-1, jump+1))
        elif curr + 5 <= e:
            find_calf.append((curr+5, jump+1))
        else:
            find_calf.append((curr+1, jump+1))

print(res)