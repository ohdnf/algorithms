import sys
sys.stdin = open('input.txt')

def affix(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return affix(n-1) + 2*affix(n-2)

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) // 10
    result = affix(N)
    print('#{} {}'.format(test_case, result))