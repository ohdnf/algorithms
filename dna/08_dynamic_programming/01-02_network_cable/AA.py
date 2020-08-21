import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in4.txt')

n = int(input())

dy = [0] * (n+1)

dy[1], dy[2] = 1, 2

for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])

# def cut(remain):
#     global res
#     if remain == 0 or remain == 1:
#         return 1
#     elif remain == 2:
#         return 2
#     else:
#         return cut(remain-1) + cut(remain-2)

# res = cut(n)
# print(res)

# res = list()

# def cut(remain, line):
#     global res
#     if remain == 0:
#         res.append(line)
#     elif remain == 1:
#         cut(0, line+'1')
#     else:
#         cut(remain-1, line+'1')
#         cut(remain-2, line+'2')

# cut(n, '')

# print(len(res))