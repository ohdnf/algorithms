import sys
input = lambda: sys.stdin.readline()

w, h = map(int, input().split())
n = int(input())
stores = [list(map(int, input().split())) for _ in range(n)]
x = list(map(int, input().split()))
x_news, x_dist = x
result = 0
for news, dist in stores:
    if x_news == news:
        result += abs(x_dist - dist)
    elif (x_news == 1 and news == 2) or (x_news == 2 and news == 1):
        result += h
        if x_dist + dist > (w * 2 - x_dist - dist):
            result += w * 2 - x_dist - dist
        else:
            result += x_dist + dist
    elif(x_news == 3 and news == 4) or (x_news == 4 and news == 3):
        result += w
        if x_dist + dist > (h * 2 - x_dist - dist):
            result += h * 2 - x_dist - dist
        else:
            result += x_dist + dist
    elif x_news == 1:   # from North
        if news == 3:   # to West
            result += x_dist + dist
        if news == 4:   # to East
            result += w - x_dist + dist
    elif x_news == 2:   # from South
        if news == 3:   # to West
            result += x_dist + h - dist
        if news == 4:   # to East
            result += w - x_dist + h - dist
    elif x_news == 3:   # from West
        if news == 1:   # to North
            result += x_dist + dist
        if news == 2:   # to South
            result += h - x_dist + dist
    elif x_news == 4:   # from East
        if news == 1:   # to North
            result += x_dist + w - dist
        if news == 2:   # to South
            result += h - x_dist + w - dist
print(result)