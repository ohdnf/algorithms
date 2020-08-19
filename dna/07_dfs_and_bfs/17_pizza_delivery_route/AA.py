import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in1.txt')

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

d = ((0, 1), (1, 0), (0, -1), (-1, 0))

house = list()  # 집
pizza = list()  # 피자집
for row in range(n):
    for col in range(n):
        if city[row][col] == 1:
            house.append((row, col))
        elif city[row][col] == 2:
            pizza.append((row, col))

total_house = len(house)
total_pizza = len(pizza)

chk = [0] * total_pizza

min_distance = float('inf')

def dfs(level, total):
    global min_distance
    if total == m or level == total_pizza:
        # 피자배달거리 계산
        curr_distance = 0

        some_pizza = [pizza[idx] for idx in range(total_pizza) if chk[idx]]
        for hrow, hcol in house:
            each_dist = float('inf')
            for prow, pcol in some_pizza:
                curr = abs(hrow-prow) + abs(hcol-pcol)
                if each_dist > curr:
                    each_dist = curr
            curr_distance += each_dist
        
        if min_distance > curr_distance:
            min_distance = curr_distance

        # print(chk, chk.count(1))
        return
    elif m - total > total_pizza - 1 - level:
        return
    else:
        chk[level] = 1
        dfs(level+1, total+1)
        chk[level] = 0
        dfs(level+1, total)

dfs(0, 0)

print(min_distance)