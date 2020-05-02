import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    N = float(input())
    print('#{} {}'.format(test_case, N))