import sys
input = lambda: sys.stdin.readline()

k = int(input())

news = []
check = ['s' for _ in range(6)]
length = []

for i in range(6):
    d, l = map(int, input().split())
    if d in news:
        check[news.index(d)] = 'd'
        check[i] = 'd'
    news.append(d)
    length.append(l)

for i in range(6):
    if check[i] == 's' and check[(i+1)%6] == 's':
        area = length[i] * length[(i+1)%6] - length[(i+3)%6] * length[(i+4)%6]

melon = area * k
print(melon)

# if check[0] == 's' and check[1] == 's':
#     big = length[0] * length[1]
#     small = length[3] * length[4]
# elif check[1] == 's' and check[2] == 's':
#     big = length[1] * length[2]
#     small = length[4] * length[5]
# elif check[2] == 's' and check[3] == 's':
#     big = length[2] * length[3]
#     small = length[5] * length[0]
# elif check[3] == 's' and check[4] == 's':
#     big = length[3] * length[4]
#     small = length[0] * length[1]
# elif check[4] == 's' and check[5] == 's':
#     big = length[4] * length[5]
#     small = length[1] * length[2]
# elif check[5] == 's' and check[0] == 's':
#     big = length[5] * length[0]
#     small = length[2] * length[3]

# melon = (big - small) * k
# print(melon)