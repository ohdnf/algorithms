import sys
input = lambda: sys.stdin.readline().rstrip()

pillars = [0 for _ in range(1001)]
N = int(input())
for _ in range(N):
    L, H = map(int, input().split())
    pillars[L] = H
peaks = []
peak = 0
for idx, height in enumerate(pillars):
    if height > peak:
        peaks = [idx]
        peak = height
    elif height == peak:
        peaks.append(idx)
area = peak * (peaks[-1] - peaks[0] + 1)
# 최정점 전까지
i_b4 = h_b4 = 0
for idx, height in enumerate(pillars):
    if height > h_b4:
        area += (idx - i_b4) * h_b4
        i_b4 = idx
        h_b4 = height
    if height == peak:
        break
# 최정점 이후부터 거꾸로
i_b4 = h_b4 = 0
for idx, height in enumerate(pillars[::-1]):
    if height > h_b4:
        area += (idx - i_b4) * h_b4
        i_b4 = idx
        h_b4 = height
    if height == peak:
        break
print(area)
