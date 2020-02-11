import sys
input = lambda: sys.stdin.readline()

line = []
total = int(input())
numbers = list(map(int, input().split()))
for idx, number in enumerate(numbers):
    if number:
        line.insert(-number, idx+1)
    else:
        line.append(idx+1)
print(' '.join(map(str, line)))