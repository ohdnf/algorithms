import sys
sys.stdin = open('input.txt')

def get_num(stack):
    if len(stack) > 1:
        num1 = int(stack.pop())
        num2 = int(stack.pop())
        return num1, num2, True
    else:
        return 0, 0, False

T = int(input())
for test_case in range(1, T+1):
    code = list(input().split())
    result = 'error'
    stack = []
    flag = True
    while flag:
        inc = code.pop(0)
        if inc == '.':
            if stack:
                result = str(stack.pop())
                if stack:
                    result = 'error'
            flag = False
        elif inc.isdigit():
            stack.append(int(inc))
        else:
            num1, num2, flag = get_num(stack)
            if flag:
                if inc == '+':
                    stack.append(num1 + num2)
                elif inc == '-':
                    stack.append(num2 - num1)
                elif inc == '*':
                    stack.append(num1 * num2)
                elif inc == '/':
                    stack.append(int(num2 / num1))
    print('#{} {}'.format(test_case, result))