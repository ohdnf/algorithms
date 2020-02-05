T = int(input())
for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    if abs(b-c) > 1 or a>0 and d>0 and b == c == 0:
        result = 'impossible'
    else:
        n = a + b + c + d + 1
        pattern = {'00': 0, '01': 0, '10': 0, '11': 0}
        result = 'impossible'
        for d in range(2**n - 1):
            b = bin(d)[2:]
            for i in range(0, len(b) - 2):
                pattern[b[i:i+2]] += 1
            if pattern['00'] == a and pattern['01'] == b and pattern['10'] == c and pattern['11'] == d:
                result = b
                break
    print('#{0} {1}'.format(test_case, result))