import sys
input = lambda: sys.stdin.readline()

def seat(k, c, r):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 1, 1
    remain = k
    direction = 0
    while remain > 0:
        x += dx[direction]
        y += dy[direction]
        if x > c and y > r and x < 0 and y < 0:
            direction += 1
            if direction == 4:
                direction = 0
        else:
            remain -= 1
    return x, y

C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)
else:
    x, y = seat(K, C, R)
    print(x, y)