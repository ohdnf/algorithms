import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numbers = sorted([int(input()) for _ in range(N)])

for number in numbers:
    print(number)