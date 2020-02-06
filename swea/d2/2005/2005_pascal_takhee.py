import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    print('#{}'.format(t))
    n = int(input())
    temp = []
    print(1)
    for i in range(n-1):
        result = [1]
        for j in range(i):
            result.append(temp[j] + temp[j+1])
        result.append(1)
        print(' '.join(map(str, result)))
        temp = result