for test_case in range(1, 11):
    width = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for i in range(2, width - 2):
        diff = buildings[i] - max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        if diff > 0:
            result += diff
    print('#{0} {1}'.format(test_case, result))