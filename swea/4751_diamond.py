T = int(input())
for t in range(1, T+1):
    string = input()
    n = len(string)
    print('..#..'+'.#..'*(n-1))
    print('.#.#.'+'#.#.'*(n-1))
    mid = '#.{}.#'.format(string[0])
    for i in range(1, n):
        mid += '.{}.#'.format(string[i])
    print(mid)
    print('.#.#.'+'#.#.'*(n-1))
    print('..#..'+'.#..'*(n-1))
