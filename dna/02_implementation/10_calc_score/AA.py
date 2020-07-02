import sys
input = lambda: sys.stdin.readline()

# sys.stdin = open('in2.txt')

n = int(input())
check = list(map(int, input().split()))
score = [0] * n

before = False
bonus = 0
for i in range(n):
    if check[i]:
        if before:
            score[i] = 1 + bonus
            bonus += 1
        else:
            score[i] = 1
            before = True
            bonus = 1
    else:
        before = False
        bonus = 0

print(sum(score))