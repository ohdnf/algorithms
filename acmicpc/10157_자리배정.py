import sys
input = lambda: sys.stdin.readline()

def seat(k, c, r):
    edge = [r, c, 1, 2]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    x, y = 1, 0
    remain = k
    while remain > 0 and x <= c and y <= r and x > 0 and y >= 0:
        x += dx[direction]
        y += dy[direction]
        remain -= 1
        # print(f'remain: {remain}, x: {x}, y: {y}, direction: {direction}')
        if direction == 0 and y == edge[direction]:
            direction += 1
            edge[0] -= 1
        elif direction == 1 and x == edge[direction]:
            direction += 1
            edge[1] -= 1
        elif direction == 2 and y == edge[direction]:
            direction += 1
            edge[2] += 1
        elif direction == 3 and x == edge[direction]:
            direction = 0
            edge[3] += 1
    return x, y

C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)
else:
    x, y = seat(K, C, R)
    print(x, y)