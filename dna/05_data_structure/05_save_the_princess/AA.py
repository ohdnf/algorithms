from collections import deque
import sys
input = lambda: sys.stdin.readline()

n, k = map(int, input().split())
princes = deque(range(1, n+1))

cnt = 0
while len(princes) > 1:
    cnt += 1
    if cnt == k:
        cnt = 0
        princes.popleft()
        # print(princes.popleft())
    else:
        princes.append(princes.popleft())

print(princes[0])