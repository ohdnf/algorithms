import copy

def solution(key, lock):
    # answer = True
    len_lock = len(lock)
    len_key = len(key)
    
    key_180 = [key[i][::-1] for i in range(len_key-1, -1, -1)]
    
    key_90 = [[0]*len_key for _ in range(len_key)]
    for col in range(len_key):
        for row in range(len_key-1, -1, -1):
            key_90[col][len_key-1-row] = key[row][col]
    
    key_270 = [key_90[i][::-1] for i in range(len_key-1, -1, -1)]

    # 전체 길이가 ((열쇠 길이 - 1) + (자물쇠 길이) + (열쇠 길이 - 1))인 행렬을 만들고 중앙에 자물쇠 모양 복사
    extension = [[0]*(2*len_key-2+len_lock) for _ in range(2*len_key-2+len_lock)]
    for row in range(len_key-1, len_key+len_lock-1):
        for col in range(len_key-1, len_key+len_lock-1):
            extension[row][col] = lock[row-len_key+1][col-len_key+1]

    for k in (key, key_90, key_180, key_270):
        # (0, 0)부터 ((열쇠 길이 - 1 + 자물쇠 길이), (열쇠 길이 - 1 + 자물쇠 길이))까지 위치 이동
        for start_row in range(0, len_key+len_lock-1):
            for start_col in range(0, len_key+len_lock-1):
                ext = copy.deepcopy(extension)  # 자물쇠 초기화

                # 자물쇠-열쇠 겹치는 부분 비교
                for row in range(start_row, start_row+len_key):
                    for col in range(start_col, start_col+len_key):
                        ext[row][col] = ext[row][col] ^ k[row-start_row][col-start_col] # XOR 연산

                # 자물쇠와 열쇠 비교 결과 확인
                answer = True
                for row in range(len_key-1, len_key+len_lock-1):
                    for col in range(len_key-1, len_key+len_lock-1):
                        if ext[row][col] == 0:
                            answer = False
                            break
                    if answer == False:
                        break
                if answer:
                    return True
    return answer

if __name__ == "__main__":
    k = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    l = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(k, l))
