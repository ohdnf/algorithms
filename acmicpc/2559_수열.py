import sys
input = lambda: sys.stdin.readline()

n, k = map(int, input().split())
temp = list(map(int, input().split()))

hap = sum(temp[:k])
result = hap
for i in range(k, n):
    hap -= temp[i-k]
    hap += temp[i]
    if hap > result:
        result = hap

print(result)