import sys
sys.stdin = open('input.txt')

def is_danzo(number):
    while number > 9:
        number, remain = number // 10, number % 10
        if number % 10 > remain:
            return False
    return True

T = int(input())
for t in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    result = -1
    for i in range(n-1):
        for j in range(i+1, n):
            now = numbers[i]*numbers[j]
            if result < now and is_danzo(now):
                result = now
    print('#{} {}'.format(t, result))