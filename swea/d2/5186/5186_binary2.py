import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    N = float(input())
    result = ''
    digits = 1
    while N > 0 and digits <= 12:
        curr = 2 ** -digits
        digits += 1
        if N - curr < 0:
            result += '0'
            continue
        N -= curr
        result += '1'
    if digits > 12 and N > 0:
        result = 'overflow'
    print('#{} {}'.format(test_case, result))