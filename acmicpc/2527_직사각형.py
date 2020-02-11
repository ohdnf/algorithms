import sys
input = lambda: sys.stdin.readline()

def check(squares):
    x1, y1, p1, q1, x2, y2, p2, q2 = squares
    if min(p1, p2) > max(x1, x2) and min(q1, q2) > max(y1, y2):
        return 'a'
    elif (min(p1, p2) == max(x1, x2) and min(q1, q2) > max(y1, y2)) or (min(p1, p2) > max(x1, x2) and min(q1, q2) == max(y1, y2)):
        return 'b'
    elif min(p1, p2) == max(x1, x2) and min(q1, q2) == max(y1, y2):
        return 'c'
    # elif min(p1, p2) < max(x1, x2) or min(q1, q2) < max(y1, y2):
    else:
        return 'd'

for _ in range(4):
    result = check(map(int, input().split()))
    print(result)


# 슈퍼컴퓨터면 가능
# def share(coord):
#     x1, y1, p1, q1, x2, y2, p2, q2 = map(int, coord)
#     x_limit = max(x1, p1, x2, p2)
#     y_limit = max(y1, y2, q1, q2)
#     matrix = [[0 for _ in range(x_limit+1)] for _ in range(y_limit+1)]
#     for row in range(y1, q1+1):
#         for col in range(x1, p1+1):
#             matrix[row][col] += 1
#     for row in range(y2, q2+1):
#         for col in range(x2, p2+1):
#             matrix[row][col] += 2
#     x_start = min(x1, p1, x2, p2)
#     y_start = min(y1, q1, y2, q2)
#     three_x = set()
#     three_y = set()
#     for row in range(y_start, y_limit+1):
#         for col in range(x_start, x_limit+1):
#             if matrix[row][col] == 3:
#                 three_x.add(col)
#                 three_y.add(row)
#     height = len(three_x)
#     width = len(three_y)
#     # a
#     if height > 1 and width > 1:
#         return 'a'
#     # b
#     elif (height == 1 and width > 1) or (height > 1 and width == 1):
#         return 'b'
#     # c
#     elif height == 1 and width == 1:
#         return 'c'
#     # d
#     else:
#         return 'd'

# for _ in range(4):
#     result = share(input().split())
#     print(result)