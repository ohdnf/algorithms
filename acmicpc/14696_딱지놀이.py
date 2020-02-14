import sys
input = lambda: sys.stdin.readline().rstrip()

# 우선 순위
# 1. 별 4
# 2. 동그라미 3
# 3. 네모 2
# 4. 세모 1
# 5. 무승부

def shobu(a, b):
    res = ['A', 'B', 'D']
    if a[4] > b[4]:
        return res[0]
    elif a[4] < b[4]:
        return res[1]
    else:
        if a[3] > b[3]:
            return res[0]
        elif a[3] < b[3]:
            return res[1]
        else:
            if a[2] > b[2]:
                return res[0]
            elif a[2] < b[2]:
                return res[1]
            else:
                if a[1] > b[1]:
                    return res[0]
                elif a[1] < b[1]:
                    return res[1]
                else:
                    return res[2]


n = int(input())
for _ in range(n):
    A = [0 for _ in range(5)]
    B = [0 for _ in range(5)]
    a_raw = input()
    b_raw = input()
    for s in a_raw[2:]:
        if s.isdigit():
            A[int(s)] += 1
    for s in b_raw[2:]:
        if s.isdigit():
            B[int(s)] += 1
    print(shobu(A, B))