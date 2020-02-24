# from collections import deque
import time
import sys
sys.stdin = open('input.txt')

start_time = time.time()

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    # queue = deque(input().split())
    queue = input().split()
    for _ in range(m):
        queue.append(queue.pop(0))
        # queue.append(queue.popleft())
    print('#{} {}'.format(test_case, queue[0]))

end_time = time.time() - start_time
print(end_time, 's')