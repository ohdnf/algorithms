from collections import permutations
import sys

# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nums = list(range(1, n+1))

