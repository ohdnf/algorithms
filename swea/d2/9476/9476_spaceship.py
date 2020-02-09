import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n, m, k, h = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    landing = 0
    for row in range(n-2):
        for col in range(m-2):
            heights = []
            for i in range(3):
                heights.extend(area[row+i][col:col+3])
            center = heights.pop(4)
            d = max(heights) - min(heights)
            e = center - min(heights)
            if d <= k and e >= 0 and e <= h:
                landing += 1
    print('#{0} {1}'.format(t, landing))
