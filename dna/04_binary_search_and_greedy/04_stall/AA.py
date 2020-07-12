import sys
input = lambda: sys.stdin.readline()

n, c = map(int, input().split())

stall = sorted([int(input()) for _ in range(n)])

def count(dist):
    horse = 1
    before = stall[0]
    for idx in range(1, n):
        if stall[idx] - before >= dist:
            horse += 1
            before = stall[idx]
    return horse

max_dist = 0
lt = 1
rt = max(stall) - min(stall)

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= c:
        max_dist = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(max_dist)
