import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    allots = list(map(int, input().split()))
    scores = {0,}
    for point in allots:
        incoming = set()
        for pre in scores:
            incoming.add(pre+point)
        scores = scores.union(incoming)
    print('#{} {}'.format(test_case, len(scores)))
