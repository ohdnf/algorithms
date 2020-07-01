import sys
input = lambda: sys.stdin.readline()
def digit_sum(number):
    return sum(list(map(int, list(number))))

# for case in range(1, 6):
#     sys.stdin = open(f'in{case}.txt')

n = int(input())
numbers = input().split()
max_sum = 0
max_num = 0
for number in numbers:
    curr = digit_sum(number)
    if max_sum < curr:
        max_sum = curr
        max_num = number
print(max_num)