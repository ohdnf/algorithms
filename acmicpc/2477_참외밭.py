import sys
input = lambda: sys.stdin.readline()

k = int(input())

news = []
distance = []
big_news = []
big_distance = []
small_news = []
small_distance = []

for _ in range(6):
    d, l = map(int, input().split())
    news.append(d)
    distance.append(l)
    if d in big_news:
        small_news.append(d)
        small_distance.append(l)
    else:
        big_news.append(d)
        big_distance.append(l)

first = small_news[0]
if first == 1:
    b1 = big_distance[big_news.index(2)]
    s1 = small_distance[0]
elif first == 2:
    b1 = big_distance[big_news.index(1)]
    s1 = small_distance[0]
elif first == 3:
    b1 = big_distance[big_news.index(4)]
    s1 = small_distance[0]
elif first == 4:
    b1 = big_distance[big_news.index(3)]
    s1 = small_distance[0]

second = small_news[1]
if second == 1:
    b2 = big_distance[big_news.index(2)]
    s2 = b2 - small_distance[1]
elif second == 2:
    b2 = big_distance[big_news.index(1)]
    s2 = b2 - small_distance[1]
elif second == 3:
    b2 = big_distance[big_news.index(4)]
    s2 = b2 - small_distance[1]
elif second == 4:
    b2 = big_distance[big_news.index(3)]
    s2 = b2 - small_distance[1]

area = b1 * b2 - s1 * s2
melon = area * k
print(melon)