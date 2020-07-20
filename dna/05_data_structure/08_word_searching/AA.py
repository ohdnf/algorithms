import sys
input = lambda: sys.stdin.readline()
n = int(input())
words = {input().strip() for _ in range(n)}
poem = {input().strip() for _ in range(n-1)}

not_used = words - poem
for word in not_used:
    print(word)
