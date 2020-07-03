import sys
input = lambda: sys.stdin.readline()

n = int(input())
a = list(map(int, input().split()))
m = int(input())
a.extend(map(int, input().split()))
a.sort()
print(*a, sep=' ')