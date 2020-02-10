import sys
input = lambda: sys.stdin.readline().rstrip()

number = int(input())
result = []
for num in range(1, number+1):
    arr = [number, num]
    while arr[-1] >= 0:
        arr.append(arr[-2] - arr[-1])
    del arr[-1]
    if len(arr) > len(result):
        result = arr

print(len(result))
print(' '.join(map(str, result)))