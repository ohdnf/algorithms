def solution(board):
    answer = 0
    last = len(board[0])

    def check(row, col, num):
        # ■□□
        # ■■■
        if row+1 < last and col+2 < last:
            if board[row][col+1] == board[row][col+2] == 0:
                if board[row+1][col] == board[row+1][col+1] == board[row+1][col+2] == num:
                    for urow in range(0, row):
                        if board[urow][col+1] or board[urow][col+2]:
                            break
                    else:
                        board[row][col] = board[row+1][col] = board[row+1][col+1] = board[row+1][col+2] = 0
                        return True
        
        # □□■
        # ■■■
        if row+1 < last and 0 <= col-2:
            if board[row][col-2] == board[row][col-1] == 0:
                if board[row+1][col-2] == board[row+1][col-1] == board[row+1][col] == num:
                    for urow in range(0, row):
                        if board[urow][col-2] or board[urow][col-1]:
                            break
                    else:
                        board[row][col] = board[row+1][col-2] = board[row+1][col-1] = board[row+1][col] = 0
                        return True
        
        # □■
        # □■
        # ■■
        if row+2 < last and 0 <= col-1:
            if board[row][col-1] == board[row+1][col-1] == 0:
                if board[row+1][col] == board[row+2][col] == board[row+2][col-1] == num:
                    for urow in range(0, row):
                        if board[urow][col-1]:
                            break
                    else:
                        board[row][col] = board[row+1][col] = board[row+2][col] = board[row+2][col-1] = 0
                        return True
        
        # ■□
        # ■□
        # ■■
        if row+2 < last and col+1 < last:
            if board[row][col+1] == board[row+1][col+1] == 0:
                if board[row+1][col] == board[row+2][col] == board[row+2][col+1] == num:
                    for urow in range(0, row):
                        if board[urow][col+1]:
                            break
                    else:
                        board[row][col] = board[row+1][col] = board[row+2][col] = board[row+2][col+1] = 0
                        return True
        
        # □■□
        # ■■■
        if row+1 < last and 0 <= col-1 and col+1 < last:
            if board[row][col-1] == board[row][col+1] == 0:
                if board[row+1][col] == board[row+1][col-1] == board[row+1][col+1] == num:
                    for urow in range(0, row):
                        if board[urow][col-1] or board[urow][col+1]:
                            break
                    else:
                        board[row][col] = board[row+1][col] = board[row+1][col-1] = board[row+1][col+1] = 0
                        return True
        
        return False
    
    while True:
        cnt = 0
        for row in range(last):
            for col in range(last):
                block_num = board[row][col]
                if block_num:
                    if check(row, col, block_num):
                        cnt += 1
        if cnt == 0:
            break
        else:
            answer += cnt

    return answer


if __name__ == "__main__":
    block = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,4,0,0,0],
        [0,0,0,0,0,4,4,0,0,0],
        [0,0,0,0,3,0,4,0,0,0],
        [0,0,0,2,3,0,0,0,5,5],
        [1,2,2,2,3,3,0,0,0,5],
        [1,1,1,0,0,0,0,0,0,5]
    ]
    res = solution(block)
    print(res)
