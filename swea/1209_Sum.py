T = int(input())
for test_case in range(1, T+1):
    numbers = [list(map(int, input().split())) for _ in range(100)]
    result, diagonal, reverse_diagonal = 0, 0, 0
    for i in range(100):
        result = max(result, sum(numbers[i]), sum([sub[i] for sub in numbers]))
        diagonal += numbers[i][i]
        reverse_diagonal += numbers[i][99-i]
    result = max(result, diagonal, reverse_diagonal)
    print('#{0} {1}'.format(test_case, result))