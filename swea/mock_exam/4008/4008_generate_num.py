import sys
sys.stdin = open('input.txt')

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

def get_operators(counts):
    oper_cnt = list(zip(('+', '-', '*', '/'), counts))
    operators = list()
    for oper, cnt in oper_cnt:
        operators.extend([oper for _ in range(cnt)])
    return operators

def generate(length, total):
    global operator
    if length == total:
        ops.append(operator)
        operator = ''
    else:
        for i in range(1, n):
            if not used[i]:
                used[i] = True
                operator += operators[i-1]
                generate(length+1, total)
                used[i] = False

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    oper_pcs = list(map(int, input().split()))
    # number_of_cases = factorial(n) // (factorial(oper_pcs[0]) * factorial(oper_pcs[1]) * factorial(oper_pcs[2]) * factorial(oper_pcs[3]))
    numbers = list(map(int, input().split()))
    operators = get_operators(oper_pcs)
    used = [False for _ in range(n)]
    operator = ''
    ops = list()
    generate(0, n)
    print(ops)