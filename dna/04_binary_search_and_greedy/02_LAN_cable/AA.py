# import sys
# input = lambda: sys.stdin.readline()

k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

lt = 1
rt = max(cables)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    for cable in cables:
        cnt += cable // mid
    if cnt >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)