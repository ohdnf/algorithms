T = int(input())
for t in range(1, T+1):
    print('#{}'.format(t))
    n = int(input())

    triangle = [[1],]
    for i in range(1, n):
        line = [1] + [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)] + [1]
        triangle.append(line)
        
    for line in triangle:
        print(' '.join(map(str, line)))