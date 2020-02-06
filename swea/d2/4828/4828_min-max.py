t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    max_num = min_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
        elif number < min_num:
            min_num = number
    print('#{0} {1}'.format(test_case, max_num - min_num))