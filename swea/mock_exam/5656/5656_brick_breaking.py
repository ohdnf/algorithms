import sys
sys.stdin = open('input.txt')

def dfs(curr, total):
    global w, h
    if curr == total:
        return
    else:
        # find first line bricks
        tops = list()
        for col in range(w):
            for row in range(h):
                if bricks[row][col]:
                    tops.append([row, col])
                    break
        for x, y in tops:
            if bricks[x][y] > 1:
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    pass
        # count splash damage
        # if splash damaged brick is more than 1, count splash damage from it
        # re-arrange bricks
        # do until there is no marble left

t = int(input())
for test_case in range(1, t+1):
    n, w, h = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(h)]
    tops = list()
    for col in range(w):
        for row in range(h):
            if bricks[row][col]:
                tops.append([row, col])
                break
    print(tops)
    print('#{} '.format(test_case))
