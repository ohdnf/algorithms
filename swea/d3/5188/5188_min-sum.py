import sys
sys.stdin = open('input.txt')

def dfs(x, y, last, hap):
    global min_sum
    if x == last and y == last:
        hap += matrix[x][y]
        if min_sum > hap:
            min_sum = hap
    elif min_sum < hap:
        return
    else:
        if x < last:
            dfs(x+1, y, last, hap+matrix[x][y])
        if y < last:
            dfs(x, y+1, last, hap+matrix[x][y])

t = int(input())
for test_case in range(1, 1+t):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 10*n*n
    dfs(0, 0, n-1, 0)
    print('#{} {}'.format(test_case, min_sum))