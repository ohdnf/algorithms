# test_case = 1

# N = int(input())

# matrix = []
# for _ in range(N):
#     row = []
#     for _ in range(N):
#         row.append(0)
#     matrix.append(row)
# x = y = 0
# number = 1
# for length in range(N, 0, -2):
#     for right in range(y, y + length):
#         matrix[x][right] = number
#         number += 1
#     y += length - 1
#     for down in range(x + 1, x + length):
#         matrix[down][y] = number
#         number += 1
#     x += length - 1
#     for left in range(y - 1, y - length, -1):
#         matrix[x][left] = number
#         number += 1
#     y -= length - 1
#     for up in range(x - 1, x - length + 1, -1):
#         matrix[up][y] = number
#         number += 1
#     x -= length - 2
#     y += 1

# print('#{0}'.format(test_case))
# for row in matrix:
#     print(' '.join(map(str, row)))

# Other Solution
T = int(input())

for i in range(1,T+1):
    N = int(input())
    print('#{}'.format(i))

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    num = 0
    index = 0

    current_x, current_y = 0, -1

    array = [[-1]*N for n in range(N)]

    while num < N*N:
        direction = directions[index]
        temp_x = current_x + direction[0]
        temp_y = current_y + direction[1]
     
        if temp_x < 0 or temp_y < 0 or temp_x >= N or temp_y >= N or array[temp_x][temp_y] != -1:
            index += 1
            if index == 4:
                index = 0
        else:
            num +=1
            current_x, current_y = temp_x, temp_y
            array[current_x][current_y] = num

    for data in array:
        print(' '.join(map(str,data)))