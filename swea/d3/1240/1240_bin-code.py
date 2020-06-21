import sys
sys.stdin = open('input.txt')

NUMBER = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
    }

t = int(input())
for case in range(1, t+1):
    N, M = map(int, input().split())
    code = None

    # 주어진 배열에서 암호코드를 추출
    for _ in range(N):
        line = input().strip('0')
        if line:
            code = line
    
    # 앞자리 0 추가
    if len(code) < 56:
        # print(len(code))
        code = '0'*(56-len(code)) + code

    # 암호코드 해독
    code_list = list()
    for idx in range(0, 56, 7):
        code_list.append(NUMBER[code[idx:idx+7]])

    # 암호코드 검증
    id_num = 0
    check_num = code_list[-1]
    for idx in range(7):
        if idx % 2:
            id_num += code_list[idx]
        else:
            id_num += code_list[idx] * 3
    
    result = 0
    if (id_num + check_num) % 10:
       pass
    else:
        result = sum(code_list)
    print('#{} {}'.format(case, result))