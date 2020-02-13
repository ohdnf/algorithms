import sys
input = lambda: sys.stdin.readline()

k = int(input())

news = []
check = ['s' for _ in range(6)]
index = []
length = []

for i in range(6):
    d, l = map(int, input().split())
    if d in news:
        check[news.index(d)] = 'd1'
        check[i] = 'd2'
    news.append(d)
    index.append(i)
    length.append(l)

print(news)
print(check)
print(index)
print(length)

# i1 = index[long_d[0]][0]
# i2 = index[long_d[1]][0]

# if (i1 == 1 and i2 == 2) or (i1 == 2 and i2 == 1):
#     s1 = distance[short_line[0]][1]
#     s2 = length[short_line[1]][1]
# elif (i1 == 2 and i2 == 3) or (i1 == 3 and i2 == 2):
#     s1 = length[short_line[0]][0]
#     s2 = length[short_line[1]][1]
# elif (i1 == 3 and i2 == 4) or (i1 == 4 and i2 == 3):
#     s1 = length[short_line[0]][0]
#     s2 = length[short_line[1]][0]
# else:
#     s1 = length[short_line[0]][1]
#     s2 = length[short_line[1]][0]

# b1 = length[long_line[0]][0]
# b2 = length[long_line[1]][0]

# area = b1 * b2 - s1 * s2
# melon = area * k
# print(melon)