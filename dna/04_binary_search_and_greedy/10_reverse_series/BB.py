import sys
input = lambda: sys.stdin.readline()

n = int(input())
rev = list(map(int, input().split()))
seq = [0] * n

for i in range(n):
    for j in range(n):
        if rev[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:
            rev[i] -= 1
print(*seq, sep=' ')