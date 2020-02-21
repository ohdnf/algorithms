import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    n = int(input())
    table = [input().split() for _ in range(n)]
    table = list(zip(*table))
    deadlocks = 0
    for line in table:
        line = ''.join(line).replace('0', '')
        deadlocks += line.count('12')
    print('#{} {}'.format(test_case, deadlocks))
