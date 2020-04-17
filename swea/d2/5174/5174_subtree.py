import sys
sys.stdin = open('input.txt')

def dfs():
    return

t = int(input())
for test_case in range(1, t+1):
    e, n = map(int, input().split())
    p_c = list(map(int, input().split()))
    adj = [list() for _ in range(e+2)]
    