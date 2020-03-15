import sys
sys.stdin = open('input.txt')

def splash(x, y):
    global w, h
    number = bricks[x][y]
    bricks[x][y] = 0
    if bricks[x][y] > 1:
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            # if splash damaged brick is more than 1, count splash damage from it
            for _ in range(number-1):
                x += dx
                y += dy
                if 0<=x<h and 0<=y<h:
                    splash(x, y)

def go(bid, last):
    global min_value, w, h
    if bid == last:
        result = w * h
        for line in bricks:
            result -= line.count(0)
        # if min_value > 

t = int(input())
for test_case in range(1, t+1):
    n, h, w = map(int, input().split()) # swap w, h to use zip()
    data = [list(map(int, input().split())) for _ in range(w)]
    bricks = [list(line) for line in list(zip(*data))]
    tops = list()
    # find first line bricks
    for row in range(h):
        for col in range(w):
            if bricks[row][col]:
                tops.append([row, col])
                break
    # do until there is no marble left
    while tops:
        x, y = tops.pop()
        # count splash damage
        splash(x, y)
        # re-arrange bricks
        for row in range(h):
            for col in range(w):
                if bricks[row][col] == 0:
                    bricks[row] = [0] + bricks[row].pop(col)
    min_value = 0
    go(0, n)
    print('#{} {}'.format(test_case, min_value))
