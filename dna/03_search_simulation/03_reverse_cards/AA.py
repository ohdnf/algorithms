import sys
input = lambda: sys.stdin.readline()

cards = list(range(0, 21))
for _ in range(10):
    s, e = map(int, input().split())
    rev = cards[e:s-1:-1]
    cards[s:e+1] = rev
cards.pop(0)
print(*cards, sep=' ')