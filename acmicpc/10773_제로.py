import sys
input = lambda: sys.stdin.readline()

ledger = []

k = int(input())
for _ in range(k):
    n = int(input())
    if n:
        ledger.append(n)
    else:
        del ledger[-1]  # 0인 경우 any(stack) == True 보장

print(sum(ledger))