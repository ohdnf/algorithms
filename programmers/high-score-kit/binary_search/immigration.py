def solution(n, times):
    answer = float('inf')
    officers = len(times)

    lt = 0
    rt = sum(map(lambda x: x*(n//officers), times))

    while lt < rt:
        mid = (lt + rt) // 2    # 주어진 시간
        passed = 0
        for time in times:
            passed += mid // time   # 각 심사관마다 심사할 수 있는 사람 수
        if passed >= n:
            if answer > mid:
                answer = mid
            rt = mid
        else:
            lt = mid + 1
    return answer


if __name__ == "__main__":
    print(solution(6, [7, 10]), 28)