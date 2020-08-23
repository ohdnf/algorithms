import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in5.txt')

n = int(input())
seq = list(map(int, input().split()))

lis = [1] * n

# DP
for i in range(1, n):
    lis[i] = 1
    for j in range(1, i):
        if seq[j] < seq[i] and 1 + lis[j] > lis[i]:
            lis[i] = 1 + lis[j]
print(max(lis))

# DP: binary search
