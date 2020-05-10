import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    incomings = list()
    for _ in range(n):
        s, e = map(int, input().split())
        incomings.append([s, e])
    incomings.sort(key=lambda t: (t[1], t[0]))
    first_truck = incomings.pop(0)
    trucks = [first_truck, ]
    while incomings:
        truck = incomings.pop(0)
        if trucks[-1][1] <= truck[0]:
            trucks.append(truck)
    print('#{} {}'.format(test_case, len(trucks)))