import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    progression = [len(one) for one in input().split('0') if one != '']
    print('#{0} {1}'.format(t, max(progression)))

# for tc in range(1, T+1):
#     N = int(input())
#     numbers = input()
#     result = 0
#     for i in range(1, N):
#         print(numbers.find('1'*i))
#         if numbers.find('1'*i) == -1:
#             result = i-1
#             break
#     print(f'#{tc} {result}')