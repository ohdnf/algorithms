# carrot.py
T = int(input())
for t in range(1, T+1):
    n = int(input())
    carrots = list(map(int, input().split()))
    result = 1      # 최대 길이
    current = 1     # 연속으로 커진 갯수
    for i in range(1, len(carrots)):
        if carrots[i-1] < carrots[i]:
            current += 1
        else:
            if current > result:
                result = current
            current = 1
    result = current
    print('#{0} {1}'.format(t, result))