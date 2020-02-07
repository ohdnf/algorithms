# 같은 숫자가 적힌 타일이 세 개 이상 있을 때는
# 빨리 벽에 닿게 될 타일을 먼저 민다

import sys
sys.stdin = open('input.txt')

def push(line):
    line = list(line)
    length = len(line)
    zeros = line.count(0)
    for _ in range(zeros):
        line.remove(0)
    zeros = 0
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            line[i] *= 2
            line[i+1] = 0
            zeros += 1
    for _ in range(zeros):
        line.remove(0)
    line.extend([0 for _ in range(length - len(line))])
    return line

def push2(line):
    line = list(line)
    n = len(line)
    result = []
    # 0 제거하기
    zeros = line.count(0)
    if zeros:
        for _ in range(zeros):
            line.remove(0)
    # 두 개 원소씩 보면서 합치기
    last = len(line) - 1
    before = 0
    for i in range(0, last + 1):
        if before:
            if before == line[i]:
                result.append(before*2)
                before = 0
            else:
                result.append(before)
                before = line[i]
                if i == last:
                    result.append(before)
        else:
            before = line[i]
            if i == last:
                result.append(before)
    zeros = n - len(result)
    result.extend([0 for _ in range(zeros)])
    return result


def transpose(tiles, direction):
    result = []
    # tiles를 push할 방향으로 회전한 뒤 복원
    if direction == 'left':
        for line in tiles:
            result.append(push(line))
        return result
    elif direction == 'right':
        for line in tiles:
            tmp = push(line[::-1])
            result.append(tmp[::-1])
        return result
    elif direction == 'up':
        for line in zip(*tiles):
            result.append(push(line))
        return list(zip(*result))
    elif direction == 'down':
        for line in zip(*tiles):
            tmp = push(line[::-1])
            result.append(tmp[::-1])
        return list(zip(*result))


T = int(input())
for test_case in range(1, T+1):
    N, direction = input().split()
    tiles = [list(map(int, input().split())) for _ in range(int(N))]
    result = transpose(tiles, direction)
    print('#{}'.format(test_case))
    for line in result:
        print(' '.join(map(str, line)))