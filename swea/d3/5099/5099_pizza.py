import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    cheeses = list(map(int, input().split()))
    pizzas = [[num+1, cheese] for num, cheese in enumerate(cheeses)]
    oven = [None for _ in range(n)]
    oven[-1] = pizzas.pop(0)
    last = None
    while any(oven):
        pizza = oven[0] # 입구에 있는 피자
        if pizza != None:
            pizza[1] //= 2  # 한 바퀴 돌 때마다 치즈 //= 2
        if pizza == None:
            if pizzas:
                oven[0] = pizzas.pop(0)
        elif pizza[1] == 0:  # 치즈가 다 녹았으면
            last = pizza
            if pizzas:  # 구울 피자 남았으면
                oven[0] = pizzas.pop(0)
            else:
                oven[0] = None
        oven.append(oven.pop(0))    # 뒤로 보내기
    print('#{} {}'.format(test_case, last[0]))