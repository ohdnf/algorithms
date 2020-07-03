import sys
input = lambda: sys.stdin.readline()

# sys.stdin = open('in2.txt')

n = int(input())
answers = list(map(int, input().split()))
# score = [0] * n

# before = False
# bonus = 0
# for i in range(n):
#     if answers[i]:
#         if before:
#             score[i] = 1 + bonus
#             bonus += 1
#         else:
#             score[i] = 1
#             before = True
#             bonus = 1
#     else:
#         before = False
#         bonus = 0
# print(sum(score))

res = cnt = 0
for answer in answers:
    if answer == 1:
        cnt += 1
        res += cnt
    else:
        cnt = 0
print(res)