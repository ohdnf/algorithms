import sys, heapq
input = lambda: sys.stdin.readline()

h = list()
while True:
    n = int(input())
    if n > 0:
        heapq.heappush(h, n)
    elif n == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(-1)
    elif n == -1:
        break

