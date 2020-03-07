import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    allots = list(map(int, input().split()))
    # scores = set()
    perfect = sum(allots)
    scores = [1] + [0] * perfect
    for point in allots:
        pre_exist = [idx for idx in range(0, perfect - point + 1) if scores[idx]]
        for idx in pre_exist:
            scores[idx + point] = 1
    result = scores.count(1)
    print('#{} {}'.format(test_case, result))
