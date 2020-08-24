import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')

n = int(input())
nums = list(map(int, input().split()))

lis = [0] * n

for i in range(1, n):
    lis[i] = 1
    for j in range(1, i):
        if nums[j] < nums[i] and lis[j] + 1 > lis[i]:
            lis[i] = lis[j] + 1
print(max(lis))