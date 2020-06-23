import sys
sys.stdin = open('input.txt')

t = int(input())

for case in range(1, t+1):
    numbers, chance = map(int, input().split())
    print('#{} {}'.format(case, numbers))