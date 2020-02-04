T = int(input())
for t in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    ascend = sorted(numbers)
    descend = sorted(numbers, reverse=True)
    result = []
    for i in range(10):
        if i % 2:
            result.append(ascend[i//2])
        else:
            result.append(descend[i//2])
    print('#{0} {1}'.format(t, ' '.join(map(str, result))))