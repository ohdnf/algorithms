import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

friends = [[] for _ in range(n)]
check = [[False for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)

# for friend in friends:
#     print(friend)

exist = False

for a in range(n):
    if friends[a]:
        for b in friends[a]:
            if not check[a][b]:
                check[a][b] = True
                if friends[b]:
                    for c in friends[b]:
                        if not check[b][c]:
                            check[b][c] = True
                            if friends[c]:
                                for d in friends[c]:
                                    if not check[c][d]:
                                        check[c][d] = True
                                        if friends[d]:
                                            exist = True
                                            break

if exist:
    print(1)
else:
    print(0)


# n, m = map(int, input().split())

# # matrix = [[] for _ in range(n)] # 인접 행렬
# matrix = [[False] for _ in range(n)] # 인접 행렬
# link = dict()                   # 인접 리스트

# for _ in range(m):
#     a, b = map(int, input().split())
#     # matrix[a].append(b)
#     link[a] = link.get(a, []) + [b]
    
#     for friend in friends:
#         result = find(friend)
# print(matrix)
# print(link)