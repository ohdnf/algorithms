def solution(m, n, puddles):
    # 지도 초기화
    area = [[0] * (m+1) for _ in range(n+1)]

    # 웅덩이 계산(좌표: (열, 행))
    for col, row in puddles:
        area[row][col] = -1

    # 가장자리 초기화
    for row in range(1, n+1):
        if area[row][1] == -1:
            break
        area[row][1] = 1
    for col in range(1, m+1):
        if area[1][col] == -1:
            break
        area[1][col] = 1

    # 최단거리 찾기
    for row in range(2, n+1):
        for col in range(2, m+1):
            if area[row][col] == -1:
                continue
            up = area[row-1][col] if area[row-1][col] != -1 else 0
            left = area[row][col-1] if area[row][col-1] != -1 else 0
            area[row][col] = left + up
    # for line in area:
    #     print(line)
    return area[n][m] % 1000000007


if __name__ == "__main__":
    # print(solution(4, 3, [[2,2]]), 4)
    # print(solution(4, 4, [[2,2]]), 8)
    print(solution(4, 4, [[2,2], [2,3]]), 5)
    # print(solution(1, 4, []), 1)
    # print(solution(5, 6, [[1,3],[3,3],[4,1]]), 40)
    # print(solution(100, 100, []), 690285631)

"""
오답 노트

주어진 좌표 = (열, 행)
"""