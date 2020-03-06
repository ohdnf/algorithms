import sys
sys.stdin = open('input.txt')

def combi(i, k, s, n, ingr):
    if i == k:
        pass
    else:
        for j in range(s, n-k+i+1):
            combi(i+1, k, j+1, n, ingr+set(j))

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]
    print('#{} '.format(test_case))
    # print(*synergy, sep='\n')
    groceries = list(range(n))
    a = list()
    b = list()
    # n개의 식재료를 두 그룹으로 나눈다 ***
    
    # 그룹 내에서 식재료마다 다른 식재료와의 시너지를 계산한다