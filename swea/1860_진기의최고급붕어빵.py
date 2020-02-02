T = int(input())
for t in range(1, T+1):
    # 예약 수(n), m초동안 k개 붕어빵 제작
    n, m, k = map(int, input().split())
    # 고객이 도착하는 시간의 배열
    eta = list(map(int, input().split()))
    # 시간마다 도착하는 고객 수
    customers = [0] * (max(eta) + 1)
    for e in eta:
        customers[e] += 1
    # 붕어빵, 방문고객 수, 가능여부 초기화
    buns = 0
    visited = customers[0]
    if visited:
        print('#{0} Impossible'.format(t))
        continue
    possible = True
    # 매초마다 만든 붕어빵과 방문고객 수 비교
    for i in range(1, len(customers)):
        if i % m == 0:
            buns += k
        visited += customers[i]
        if visited > buns:
            possible = False
            break
    if possible:
        print('#{0} Possible'.format(t))
    else:
        print('#{0} Impossible'.format(t))