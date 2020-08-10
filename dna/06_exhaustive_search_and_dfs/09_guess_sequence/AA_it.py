import sys
import itertools as it
sys.stdin = open('in1.txt')
n, f = map(int, input().split())
coef = [1] * n
for i in range(1, n):
    coef[i] = coef[i-1] * (n-1)/i
a = list(range(1, n+1))
for tmp in it.permutations(a, 3):
    sum = 0
    for i, x in enumerate(tmp):
        sum += x * coef[i]
    if sum == f:
        print(*tmp)
        break
