import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in4.txt')

n = int(input())

dy = [0] * (n+1)

# Bottom-up

# dy[1], dy[2] = 1, 2

# for i in range(3, n+1):
#     dy[i] = dy[i-1] + dy[i-2]

# print(dy[n])



# Top-down

def cut(remain):
    if remain == 1 or remain == 2:
        return remain

    # Memoization
    if dy[remain]:
        return dy[remain]
    else:
        dy[remain] = cut(remain-1) + cut(remain-2)
        return dy[remain]

print(cut(n))