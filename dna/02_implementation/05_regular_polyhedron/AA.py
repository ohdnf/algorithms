import sys
input = lambda: sys.stdin.readline()
# for case in range(1, 6):
#     sys.stdin = open(f'in{case}.txt')

n, m = map(int, input().split())
total = n * m
numbers = {num: 0 for num in range(2, n+m+1)}
for i in range(1, n+1):
    for j in range(1, m+1):
        numbers[i+j] += 1

max_count = 0
max_nums = set()
for num, cnt in numbers.items():
    if cnt > max_count:
        max_count = cnt
        max_nums = {num, }
    elif cnt == max_count:
        max_nums.add(num)
numbers = sorted(list(max_nums))
print(*numbers, sep=' ')