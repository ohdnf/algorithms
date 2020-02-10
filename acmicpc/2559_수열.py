import sys
input = lambda: sys.stdin.readline()

n, k = map(int, input().split())
temp = list(map(int, input().split()))

hap = [sum(temp[i:i+k]) for i in range(1, n-k+1)]
print(max(hap))