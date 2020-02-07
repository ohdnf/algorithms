import sys
sys.stdin = open('input.txt')

def count(puzzle, word):
    result = 0
    for line in puzzle:
        line = line.split('0')
        result += line.count(word)
    return result

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    word = '1'*k    # 단어 길이
    puzzle = [input().replace(' ', '') for _ in range(n)]
    result = count(puzzle, word)
    vertical = [''.join(line) for line in list(zip(*puzzle))]   # 세로 방향
    result += count(vertical, word)
    print('#{0} {1}'.format(t, result))