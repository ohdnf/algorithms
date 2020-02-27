import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n, b = map(int, input().split())    # 점원 수, 선반 높이
    clerks = list(map(int, input().split()))
    # clerks.sort(reverse=True)
    heights = list()
    for i in range(1<<n):
        tmp = 0
        for j in range(n+1):
            if i & (1<<j):
                tmp += clerks[j]
        if tmp >= b:
            heights.append(tmp - b)
    heights.sort()
    print('#{} {}'.format(test_case, heights[0]))
