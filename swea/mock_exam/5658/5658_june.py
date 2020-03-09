import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input()
    d = N//4
    arr = []
    for i in range(d):                  # 각 변에 있는 숫자의 시작 인덱스
        for j in range(4):              # 뚜껑의 각 면
            s = ''
            for p in range(d):          # 한 면의 글자를 순서대로
                s += num[(i + j*d + p)%N]
            if int(s, 16) not in arr:
                arr.append(int(s, 16))
    arr.sort(reverse=True)
    print('#{} {}'.format(tc, arr[K-1]))