import sys
sys.stdin = open('input.txt')

t = int(input())

for case in range(1, t+1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    houses = []
    stores = []
    for row in range(n):
        for col in range(n):
            if area[row][col] == 0:
                continue
            elif area[row][col] == 1:
                houses.append((row, col))
            else:
                stores.append((row, col))
    # print('houses', houses)
    # print('stores', stores)
    min_cost = float('inf')
    # 주어진 음식배달집을 운영하는 모든 경우의 수
    for i in range(1, 1 << len(stores)):
        curr_stores = []
        cost = 0
        for j in range(len(stores)):
            if i & 1 << j:
                curr_stores.append(stores[j])
                cost += area[stores[j][0]][stores[j][1]]
        # print('curr_stores', curr_stores)

        # 집마다 현재 운용 중인 배달집 중 가장 가까운 배달집 찾기
        for house in houses:
            min_distance = float('inf')
            for store in curr_stores:
                distance = abs(store[0] - house[0]) + abs(store[1] - house[1])
                if min_distance > distance:
                    min_distance = distance
            cost += min_distance
        if min_cost > cost:
            min_cost = cost
        # print('cost', cost)
        # print('min_cost', min_cost)

    print('#{0} {1}'.format(case, min_cost))
