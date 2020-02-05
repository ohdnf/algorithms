T = int(input())
for t in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    danzo = []
    for i in range(n-1):
        for j in range(i+1, n):
            cur = numbers[i]*numbers[j]
            good = True
            while cur > 9:
                first = cur % 10
                cur //= 10
                second = cur % 10
                if first < second:
                    good = False
                    break
            if good:
                danzo.append(numbers[i]*numbers[j])
    if not danzo:
        danzo.append(-1)
    print('#{} {}'.format(t, max(danzo)))