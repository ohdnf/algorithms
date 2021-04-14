from collections import deque
import sys

N, K = map(int, input().split())

if N == K:
    print(0)
    sys.exit()

dist = [[-1, -1] for _ in range(500001)]

queue = deque()
queue.append((N, 0))
dist[N][0] = 0
while queue:
    curr_loc, parity = queue.popleft()
    for next_loc in (curr_loc - 1, curr_loc + 1, curr_loc * 2):
        if 0 <= next_loc <= 500000:
            if dist[next_loc][1 - parity] == -1:
                dist[next_loc][1 - parity] = dist[curr_loc][parity] + 1
                queue.append((next_loc, 1 - parity))

answer = -1
elapsed = 0
while True:
    K += elapsed
    if K > 500000:
        break
    if dist[K][elapsed % 2] <= elapsed:
        answer = elapsed
        break
    elapsed += 1

print(answer)

# subin = set([N,])
# target = K
# second = 0

# while True:
#     second += 1
#     new_subin = set()
#     for now in subin:
#         if 1 <= now:
#             new_subin.add(now - 1)
#         if now <= 499999:
#             new_subin.add(now + 1)
#         if now <= 250000:
#             new_subin.add(now * 2)
#     target += second
#     if target > 500000:
#         second = -1
#         break
#     if target in new_subin:
#         break
#     subin = new_subin

# print(second)
