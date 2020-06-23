import sys
sys.stdin = open('input.txt')

def check(code):
    # 암호코드 검증
    chk = res = code[-1]
    for i in range(7):
        if i % 2:
            chk += code[i]
        else:
            chk += code[i] * 3
        res += code[i]
    if chk % 10:
        return 0
    else:
        return res

t = int(input())
for case in range(1, t+1):
    N, M = map(int, input().split())
    data = set()
    for _ in range(N):
        line = input().strip('0')
        if line:
            data.add(line)
    for line in data:
        line = bin(int(line, 16))[2:].strip('0')
        
    print('#{} {}'.format(case, len(data)))