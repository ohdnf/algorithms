import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
guitars = []
for _ in range(N):
    serial = input()
    hap = 0
    for char in serial:
        if char.isdigit():
            hap += int(char)
    guitars.append([len(serial), hap, serial])

guitars = sorted(guitars, key=lambda g: (g[0], g[1], g[2]))

for _, _, serial in guitars:
    print(serial)