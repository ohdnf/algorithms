import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n = int(input())    # 버스 노선 수
    lines = list()      # 버스 노선
    for _ in range(n):
        start, end = map(int, input().split())  # 기점, 종점
        lines.append(range(start, end+1))
    p = int(input())    # 정류장 수
    counts = list()     # 정류장별 버스 노선 수
    for _ in range(p):
        stop = int(input()) # 정류장 번호
        count = 0           # 지나는 버스 노선 수
        for line in lines:
            if stop in line:
                count += 1
        counts.append(count)
    
    print('#{}'.format(test_case), end=' ')
    print(*counts, sep=' ')