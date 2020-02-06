import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    print('#{}'.format(t))
    n = int(input())
    print(1)
    prev_line = [0, 1, 0]
    for length in range(2, n+1):
        curr_line = [0] + [prev_line[i] + prev_line[i+1] for i in range(length)] + [0]
        print(' '.join([str(n) for n in curr_line[1:-1]]))
        prev_line = curr_line