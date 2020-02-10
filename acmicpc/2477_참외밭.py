import sys
input = lambda: sys.stdin.readline()

k = int(input())    # 1제곱미터 안 참외 수

news = [None for _ in range(5)]
width = height = small_w = small_h = 0
for _ in range(6):
    d, l = map(int, input().split())
    # 두번째 등장
    if news[d]:
        # 두번째 등장의 두번째
        if news[0]:
            if d == 1:
                width = news[d+1]
                small_w = width - l
            elif d == 2:
                width = news[d-1]
                small_w = width - l
            elif d == 3:
                height = news[d+1]
                small_h = height - l
            elif d == 4:
                height = news[d-1]
                small_h = height - l
        # 두번째 등장의 첫번째
        else:
            news[0] = True
            # 반대편 긴 변을 큰 사각형의 변으로 지정
            if d == 1:
                width = news[d+1]
                small_w = l
            elif d == 2:
                width = news[d-1]
                small_w = l
            elif d == 3:
                height = news[d+1]
                small_h = l
            elif d == 4:
                height = news[d-1]
                small_h = l
    # 첫 등장
    else:
        news[d] = l

melon = (width * height - small_w * small_h) * k
print(melon)

# E:1 W:2 S:3 N:4
# dy = [0, 0, 0, 1, -1]
# dx = [0, 1, -1, 0, 0]

# field = 1
# first = corner[0]
# if first[0] == 1 or first[0] == 3:
#     field *= news[first[0]]
# else:
#     field *= news[first[0]-2]
# second = corner[1]
# if second[0] == 1 or second[0] == 3:
#     field *= news[second[0]]
#     small = first[1] * (news[second[0]] - second[1])
#     field -= small
# else:
#     field *= news[second[0]-2]
#     small = first[1] * (news[second[0]-2] - second[1])
#     field -= small
# melon = field * k
# print(melon)

# hy = [0]
# hx = [0]
# for _ in range(6):
#     d, l = map(int, input().split())
#     hy.append(hy[-1] + dx[d] * l)
#     hx.append(hx[-1] + dy[d] * l)

# width = abs(max(hx) - min(hx))
# height = abs(max(hy) - min(hy))
# print(width, height)

# for i in range(1, 6):
#     # E
#     if hy[i-1] == hy[i] and hx[i-1] < hx[i]:
#         pass
#     # W
#     elif hy[i-1] == hy[i] and hx[i-1] > hx[i]:
#         pass
#     # S
#     elif hy[i-1] > hy[i] and hx[i-1] == hx[i]:
#         pass
#     # N
#     elif hy[i-1] < hy[i] and hx[i-1] == hx[i]:
#         pass

