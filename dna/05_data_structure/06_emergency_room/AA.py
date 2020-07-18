from collections import deque
import sys
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
waiting = deque((num, risk) for num, risk in enumerate(map(int, input().split())))

# print(max(waiting, key=lambda w:w[1]))
order = 0

while waiting:
    curr = waiting.popleft()
    # if any(curr[1] < remain[1] for remain in waiting):
    if curr[1] < max(waiting, key=lambda w:w[1])[1]:
        waiting.append(curr)
        continue
    order += 1
    if curr[0] == m:
        print(order)
        break
