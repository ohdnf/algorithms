import sys
input = lambda: sys.stdin.readline()

t = int(input())
for test_case in range(1, t+1):
    n, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    part = sorted(numbers[s-1:e])
    print(part[k-1])