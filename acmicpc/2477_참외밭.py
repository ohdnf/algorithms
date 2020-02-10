import sys
input = lambda: sys.stdin.readline()

# E:1 W:2 S:3 N:4
dy = [0, 0, 0, 1, -1]
dx = [0, 1, -1, 0, 0]

k = int(input())
hy = [0]
hx = [0]
for _ in range(6):
    d, l = map(int, input().split())
    hy.append(hy[-1] + dx[d] * l)
    hx.append(hx[-1] + dy[d] * l)

width = abs(max(hx) - min(hx))
height = abs(max(hy) - min(hy))
# print(width, height)

for i in range(1, 6):
    # E
    if hy[i-1] == hy[i] and hx[i-1] < hx[i]:
        pass
    # W
    elif hy[i-1] == hy[i] and hx[i-1] > hx[i]:
        pass
    # S
    elif hy[i-1] > hy[i] and hx[i-1] == hx[i]:
        pass
    # N
    elif hy[i-1] < hy[i] and hx[i-1] == hx[i]:
        pass

