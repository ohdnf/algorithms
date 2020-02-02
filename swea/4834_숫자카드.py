T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = input()
    counts = [0] * 10
    for card in cards:
        counts[int(card)] += 1
    freq = num = 0
    for i, c in enumerate(counts[::-1]):
        if c > freq:
            freq = c
            num = 9 - i
    print('#{0} {1} {2}'.format(t, num, freq))
    