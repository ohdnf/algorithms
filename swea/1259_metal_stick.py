# import sys
# sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    d = list(map(int, input().split()))
    
    nuts = [[] for _ in range(max(d)+1)]
    screws = []
    for i in range(0, n*2, 2):
        screws.append((d[i], d[i+1]))
        nuts[d[i]].append(d[i+1])
    
    used = [[False] for _ in range(max(d)+1)]
    sticks = []
    for screw in screws:
        bolt = screw[0]
        stick = ''
        def connect(bolt):
            global stick
            used[bolt] = True
            stick += '{} '.format(bolt)
            connect(nuts[bolt])
        connect(bolt)
        sticks.append(stick)
    print(sticks)
    # candidates = []
    # for screw in screws:
    #     stack = []
    #     def connect(screw):
    #         now = screw
    #         stack.append(screw)
    #         screws.remove(screw)
    #         for nxt in screws:
    #             if now[1] == nxt[0]:
    #                 connect(nxt)
    #         stack.pop(screw)
    #         screws.append(screw)
    #         return
    