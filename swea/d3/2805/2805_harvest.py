# import sys
# sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    center = n // 2
    result = 0
    i = 0
    for j in range(n):
        line = farm[j]
        result += sum(line[center-i:center+i+1])
        if j < center:
            i += 1
        else:
            i -= 1
    print('#{0} {1}'.format(t, result))