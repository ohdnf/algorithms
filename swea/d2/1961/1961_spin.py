import sys
sys.stdin = open('input.txt')

def show(matrix):
    for line in matrix:
        print(line)

def turn_90(matrix):
    return [[matrix[n-j-1][i] for j in range(n)] for i in range(n)]

def turn_180(matrix, n):
    return [[matrix[n-i-1][n-j-1] for j in range(n)] for i in range(n)]
    
def turn_270(matrix):
    # return list(zip(*[line[::-1] for line in matrix]))
    return [[matrix[j][n-i-1] for j in range(n)] for i in range(n)]

T = int(input())
for t in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # show(matrix)
    matrix_90 = turn_90(matrix)
    # show(matrix_90)
    matrix_180 = turn_180(matrix, n)
    # show(matrix_180)
    matrix_270 = turn_270(matrix)
    # show(matrix_270)
    print('#{}'.format(t))
    for i in range(n):
        print(''.join(map(str, matrix_90[i])), end=' ')
        print(''.join(map(str, matrix_180[i])), end=' ')
        print(''.join(map(str, matrix_270[i])))

# # 과거의 나
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     matrix = []
#     for row in range(N):
#         matrix.append(list(map(int, input().split())))
    
#     matrix_90 = []
#     for row in range(N):
#         line = []
#         for col in range(N):
#             line.append(matrix[N-col-1][row])
#         matrix_90.append(line)
    
#     matrix_180 = []
#     matrix_270 = []
#     for row in range(N-1, -1, -1):
#         matrix_180.append(matrix[row][::-1])
#         matrix_270.append(matrix_90[row][::-1])
    
#     print('#{0}'.format(test_case))
#     for row in range(N):
#         line = []
#         for m in [matrix_90, matrix_180, matrix_270]:
#             line.append(''.join(map(str, m[row])))
#         print(' '.join(line))

# # 실행시간 젤 빠른 코드
# T = int(input())
# for test_case in range(1,T+1):
#     print("#{}".format(test_case))
#     n=int(input())
#     arr=[]
#     dir=[90,180,270]
#     for _ in range(n):
#         arr.append(list(input().split()))
#     for i in range(n):
#         result=""
#         for case in dir:
#             if case == 90:
#                 for j in range(n-1,-1,-1):
#                     result+=arr[j][i]
#                 result += " "
#             elif case == 180:
#                 for j in range(n-1,-1,-1):
#                     result+=arr[n-1-i][j]
#                 result += " "
#             elif case == 270:
#                 for j in range(0,n):
#                     result+=arr[j][n-1-i]
#         print(result)