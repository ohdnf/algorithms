import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    hexa = input()
    numbers = set()
    interval = n // 4
    for _ in range(interval):
        for idx in range(0, n, interval):
            numbers.add(int(hexa[idx:idx+interval], 16))
        hexa = hexa[-1] + hexa[:-1]
    numbers = sorted(list(numbers), reverse=True)
    print('#{} {}'.format(test_case, numbers[k-1]))