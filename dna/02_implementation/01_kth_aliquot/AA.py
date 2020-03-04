import sys
input = lambda: sys.stdin.readline()

whole, k = map(int, input().split())
aliquots = [num for num in range(1, whole+1) if whole % num == 0]
l = len(aliquots)
if k > l:
    print(-1)
else:
    print(aliquots[k-1])