from collections import deque
import sys
input = lambda: sys.stdin.readline()

n = int(input())
nums = deque(map(int, input().split()))

last = 0
res = ''

while nums and (nums[0] > last or nums[-1] > last):
    if (nums[0] < last < nums[-1]) or (last < nums[-1] < nums[0]):
        res += 'R'
        last = nums.pop()
    else:
        res += 'L'
        last = nums.popleft()

print(len(res))
print(res)