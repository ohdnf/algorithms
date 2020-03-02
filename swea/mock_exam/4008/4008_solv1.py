import sys
sys.stdin = open('input.txt')

def calc(idx, length, last, op1, op2, op3, op4):
    global min_val, max_val
    if idx == length:
        if last < min_val:
            min_val = last
        if last > max_val:
            max_val = last
    else:
        if op1 > 0:
            calc(idx+1, length, last + numbers[idx], op1-1, op2, op3, op4)
        if op2 > 0:
            calc(idx+1, length, last - numbers[idx], op1, op2-1, op3, op4)
        if op3 > 0:
            calc(idx+1, length, last * numbers[idx], op1, op2, op3-1, op4)
        if op4 > 0:
            calc(idx+1, length, int(last/numbers[idx]), op1, op2, op3, op4-1)

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    op1, op2, op3, op4 = map(int, input().split())  # +, -, *, /
    numbers = list(map(int, input().split()))
    length = len(numbers)
    min_val = 100000000
    max_val = -100000000
    calc(1, length, numbers[0], op1, op2, op3, op4)
    print('#{} {}'.format(test_case, max_val - min_val))
