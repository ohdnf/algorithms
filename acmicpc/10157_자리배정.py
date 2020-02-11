import sys
input = lambda: sys.stdin.readline()

def seat(k, c, r):
    edge = [r, c, 0, 0]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 1, 1
    remain = k
    turn = 0
    while k > 0 and x <= edge[0] and y <= edge[1] and x >= edge[2] and y >= edge[3]:
        # 마지막까지 돌자
        pass
    return x, y

C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)
else:
    x, y = seat(K, C, R)