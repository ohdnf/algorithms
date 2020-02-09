import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    cnts = list(map(int, input().split()))
    stems = 0       # 긴 줄기 수
    max_length = 0  # 가장 긴 줄기
    max_total = 0   # 가장 긴 줄기의 고구마 갯수
    length = 0      # 현재 줄기 길이
    total = 0       # 현재 줄기의 고구마 갯수
    before = 0      # 왼쪽 구역의 고구마 갯수
    for c in cnts:
        if before:
            if before < c:  # 긴 줄기 연속
                length += 1
                total += c
            else:   # 긴 줄기 종료
                if length > 1:  # 긴 줄기면
                    stems += 1
                    if length > max_length:
                        max_length = length
                        max_total = total
                    elif length == max_length:
                        if total > max_total:
                            max_total = total
                length = 1  # 현재 구역부터 다시 초기화
                total = c
        else:
            length = 1
            total = c
        before = c
    if length > 1:
        stems += 1
        if length > max_length:
            max_length = length
            max_total = total
        elif length == max_length:
            if total > max_total:
                max_total = total
    print('#{0} {1} {2}'.format(t, stems, max_total))