import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    horizon = []
    for _ in range(5):
        line = input()
        if len(line) < 15:
            line += ' ' * (15 - len(line))
        horizon.append(line)
    
    vertical = list(zip(*horizon))
    result = ''
    for line in vertical:
        result += ''.join(line)
    result = result.replace(' ', '')
    print('#{0} {1}'.format(t, result))