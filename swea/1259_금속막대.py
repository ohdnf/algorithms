import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    d = list(map(int, input().split()))
    screws = []
    for i in range(0, n*2, 2):
        screws.append((d[i], d[i+1]))
    candidates = []
    for screw in screws:
        stack = []
        def connect(screw):
            now = screw
            stack.append(screw)
            screws.remove(screw)
            for nxt in screws:
                if now[1] == nxt[0]:
                    connect(nxt)
            stack.pop(screw)
            screws.append(screw)
            return
    
    print(screws)