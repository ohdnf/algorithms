N = int(input())

# print('\n'.join(map(str, matrix)))

def move(N):
    matrix = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(0)
        matrix.append(row)
    x = y = 0
    number = 1
    for step in range(N, 1, -2):
        for right in range(y, step):
            matrix[x][right] = number
            number += 1
        y += step - 1
        for down in range(x + 1, step):
            matrix[down][y] = number
            number += 1
        x += step - 1
        for left in range(y - 1, y - step, -1):
            matrix[x][left] = number
            number += 1
        y -= step - 1
        for up in range(x - 1, x - step + 1, -1):
            matrix[up][y] = number
            number += 1
        x -= step - 2
        y += 1
    return matrix
if N % 2:
    result = move(N)
else:
    result = move(N)
print('\n'.join(map(str,result)))