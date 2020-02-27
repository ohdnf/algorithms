import sys
sys.stdin = open('input.txt')

def stack(height, shelf):
    if height >= shelf:
        heights.append(height)
    else:
        pass

t = int(input())
for test_case in range(1, t+1):
    n, b = map(int, input().split())    # 점원 수, 선반 높이
    clerks = list(map(int, input().split()))
    loaded = [False for _ in range(n+1)]
    heights = list()
    # stack(clerks[0], b)
    print('#{} {}'.format(test_case, heights[0]))
