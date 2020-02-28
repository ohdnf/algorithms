import sys
sys.stdin = open('input.txt')
# sys.stdin = open('swea/mock_exam/4008/input.txt')


def permute(idx, total):
    if len(tmp) == total - 1:
        operators.append(tmp[:])
        tmp.clear()
    else:
        used[idx] = True
        tmp.append(operator[idx])
        for j in range(n-1):
            if not used[j]:
                permute(j, total)
        used[idx] = False

def generate(nums, ops):
    while ops:
        now = ops.pop()
        tmp = nums[:]
        stack = list()
        while now:
            op = ops.pop(0)
            if stack and tmp:
                front = stack.pop(0)
                back = tmp.pop(0)
                if op == '+':
                    front += back
                elif op == '-':
                    front -= back
                elif op == '*':
                    front *= back
                elif op == '/':
                    front //= back
                stack.append(front)
            else:   # First number
                stack.append(tmp.pop(0))
        results.append(stack[0])


t = int(input())
for test_case in range(1, t+1):
    n = int(input())    # 숫자의 갯수
    plus, minus, multi, divide = map(int, input().split())
    numbers = list(map(int, input().split()))
    operator = ['+'] * plus + ['-'] * minus + ['*'] * multi + ['/'] * divide
    operators = list()
    tmp = list()
    used = [False for _ in range(n-1)]
    for i in range(n-1):
        permute(i, n)
    results = list()
    generate(numbers, operators)
    print('#{} {}'.format(test_case, results))
