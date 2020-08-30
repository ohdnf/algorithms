import sys
# sys.stdin = open('in3.txt')

n = int(input())    # 회원 수
D = [[float('inf')]*n for _ in range(n)]    # 친구 관계

while True:
    s, e = map(int, input().split())
    if s == -1 and e == -1:
        break
    D[s-1][e-1] = 1
    D[e-1][s-1] = 1

F = [0]*n   # 회원의 점수

for k in range(n):
    for i in range(n):
        if i != k:
            for j in range(n):
                if i == j:
                    D[i][j] = 0
                elif j != i and j != k:
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                    # print(i, j, D[i][j])
                    # if D[i][j] != float('inf') and F[i] < D[i][j]:
                    #     F[i] = D[i][j]

# for line in D:
#     print(line)

candidates = list()
min_score = float('inf')

for i in range(n):
    score = max(D[i])
    if min_score > score:
        min_score = score
        candidates.clear()
        candidates.append(i+1)
    elif min_score == score:
        candidates.append(i+1)


# for i in range(n):
#     if min_score > F[i]:
#         min_score = F[i]
#         candidates.clear()
#         candidates.append(i+1)
#     elif min_score == F[i]:
#         candidates.append(i+1)
# print(F)

print(min_score, len(candidates))
print(*candidates)