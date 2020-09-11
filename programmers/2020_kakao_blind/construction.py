def solution(n, build_frame):
    # n: 벽면의 크기
    # build_frame: 기둥과 보를 설치하거나 삭제하는 작업이 담긴 2차원 배열
    # build_frame의 원소: [x, y, a, b] (각각 가로 좌표, 세로 좌표, 기둥/보, 삭제/설치)

    board = [[[0, 0] for _ in range(n+1)] for _ in range(n+1)]
    # ----------------------바닥----------------------
    # [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    # [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    # [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    # [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    # [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    # [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    # 기둥 규칙
    def col_status(x, y):
        if x == 0:  # 바닥 위
            return True
        if 0 <= x-1 and board[x-1][y][0]:   # 다른 기둥 위
            return True
        if board[x][y][1] or (0 <= y-1 and board[x][y-1][1]):   # 다른 보 위
            return True
        return False

    # 보 규칙
    def beam_status(x, y):
        if 0 <= x-1 and (board[x-1][y][0] or board[x-1][y+1][0]):   # 다른 기둥 위
            return True
        if (0 <= y-1 and board[x][y-1][1]) and (y+1 <= n and board[x][y+1][1]): # 양쪽 끝 부분이 다른 보와 연결
            return True
        return False

    for y, x, a, b in build_frame:
        # 열 =>  x / 행 => y
        # a: 0(기둥), 1(보)
        # b: 0(삭제), 1(설치)
        if a == 0 and b == 0:   # 기둥 삭제
            board[x][y][0] = 0
            # (x+1, y) 기둥 검사
            if x+1 <= n and board[x+1][y][0]:   
                if not col_status(x+1, y):
                    board[x][y][0] = 1
                    continue
            #  (x+1, y) 보 검사
            if x+1 <= n and board[x+1][y][1]:
                if not beam_status(x+1, y):
                    board[x][y][0] = 1
                    continue
            # (x+1, y-1) 보 검사
            if x+1 <= n and 0 <= y-1 and board[x+1][y-1][1]:
                if not beam_status(x+1, y-1):
                    board[x][y][0] = 1
        elif a == 0 and b == 1:     # 기둥 설치
            if col_status(x, y):
                board[x][y][0] = 1
        elif a == 1 and b == 0:     # 보 삭제
            board[x][y][1] = 0
            # (x, y) 기둥 검사
            if board[x][y][0]:
                if not col_status(x, y):
                    board[x][y][1] = 1
                    continue
            # (x, y+1) 기둥 검사
            if y+1 <= n and board[x][y+1][0]:
                if not col_status(x, y+1):
                    board[x][y][1] = 1
                    continue
            # (x, y-1) 보 검사
            if 0 <= y-1 and board[x][y-1][1]:
                if not beam_status(x, y-1):
                    board[x][y][1] = 1
                    continue
            # (x, y+1) 보 검사
            if y+1 <= n and board[x][y+1][1]:
                if not beam_status(x, y+1):
                    board[x][y][1] = 1
        elif a == 1 and b == 1:    # 보 설치
            if beam_status(x, y):
                board[x][y][1] = 1

    # 구조물 상태 읽기
    answer = list()
    for x in range(n+1):
        for y in range(n+1):
            for a, is_built in enumerate(board[x][y]):
                if is_built:
                    answer.append([y, x, a])
    
    # 최종 구조물의 상태: [가로 좌표, 세로 좌표, 구조물 종류(0: 기둥, 1: 보)]
    # 정렬 기준: 가로 좌표 기준 오름차순 > 세로 좌표 기준 오름차순 > 기둥 다음 보
    answer.sort(key=lambda frame: (frame[0], frame[1], frame[2]))

    return answer


if __name__ == "__main__":
    res1 = solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
    print(res1)
    print()
    res2 = solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
    print(res2)