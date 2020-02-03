for _ in range(1, 11):
    test_case = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]             # 주어진 행렬
    jux_nums = [[numbers[j][i] for j in range(100)] for i in range(100)]        # 전치행렬

    # 최댓값, 좌상향, 우상향 대각선 초기화
    result = l_diag = r_diag = 0

    for i in range(100):
        # 행의 합
        row = 0
        for num in numbers[i]:
            row += num
        # 열의 합
        col = 0
        for num in jux_nums[i]:
            col += num
        
        # 최댓값 비교
        if row > result:
            result = row
        if col > result:
            result = col
        
        # 대각선의 합
        l_diag += numbers[i][i]     # 좌상향
        r_diag += jux_nums[i][i]    # 우상향

    # 최댓값 비교
    if l_diag > result:
        result = l_diag
    if r_diag > result:
        result = r_diag
    print('#{0} {1}'.format(test_case, result))