num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = list()

for n in num:
    while stack and m and stack[-1] < n:
        stack.pop()
        m -= 1
    stack.append(n)

while m:
    stack.pop()
    m -= 1
print(*stack, sep='')