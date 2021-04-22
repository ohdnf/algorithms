n, k = map(int, input().split())

josephus = 0
for idx in range(1, n):
    josephus = (josephus + k) % (idx + 1)

print(josephus + 1)
