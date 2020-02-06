T = int(input())
for t in range(1, T+1):
    # 버스 최대이동거리, 종점 번호, 충전기 수
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))

    bus = K
    fuel = K
    cnt = 0

    while bus < N:
        if bus in charges:
            charges.remove(bus)
            cnt += 1
            bus += K
            fuel = K
        else:
            if fuel > 0:
                bus -= 1
                fuel -= 1
            else:
                cnt = 0
                break
    
    print('#{0} {1}'.format(t, cnt))
