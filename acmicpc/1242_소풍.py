n, k, m = map(int, input().split())

# 방법 1
# 나머지 연산을 위해 인덱스를 1...n에서 0...(n-1)로 변경
# m -= 1
# start = 0
# out = 0

# while True:
#     next_out = (start + k - 1) % n
#     out += 1
#     if next_out == m:
#         break
#     elif next_out < m:
#         m -= 1
#     n -= 1
#     start = next_out

# print(out)


# 방법 2
# 사람이 탈락할 때마다 다음 사람부터 번호 1로 다시 시작
out = 0
while True:
    out += 1
    m -= k
    while m < 0:
        m += n
    if m == 0:
        break
    n -= 1
print(out)
