T = int(input())
for t in range(1, T+1):
    # 예약 수(n), m초동안 k개 붕어빵 제작
    n, m, k = map(int, input().split())
    # 손님이 도착하는 시간의 배열
    ETA = list(map(int, input().split()))
    cnt = [0] * max(ETA+1)
    for eta in ETA:
        cnt[eta] += 1
    