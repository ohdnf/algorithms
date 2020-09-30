def solution(triangle):
    dp = [[0] * (i+1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]   # 꼭대기 수 초기화

    for level in range(1, len(triangle)):
        for idx in range(level+1):  # level: 0 ... len(triangle)-1  / idx: 0 ... level
            if idx == 0:
                dp[level][idx] = dp[level-1][idx] + triangle[level][idx]
            elif idx == level:
                dp[level][idx] = dp[level-1][idx-1] + triangle[level][idx]
            else:
                dp[level][idx] = max(dp[level-1][idx-1] + triangle[level][idx], dp[level-1][idx] + triangle[level][idx])

    return max(dp[-1])


if __name__ == "__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]), 30)