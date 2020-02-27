import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    # 수열의 길이, 편집 횟수, 출력할 인덱스
    n, m, l = map(int, input().split())
    seq = input().split()

    for _ in range(m):
        cmd, *num = input().split()
        if cmd == 'I':
            seq.insert(int(num[0]), num[1])
        elif cmd == 'D':
            seq.pop(int(num[0]))
        elif cmd == 'C':
            seq[int(num[0])] = num[1]
    
    result = -1
    if l < len(seq):
        result = seq[l]
    print('#{} {}'.format(test_case, result))
