import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    progression = [len(one) for one in input().split('0') if one != '']
    print('#{0} {1}'.format(t, max(progression)))
    