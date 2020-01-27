T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    len_n = len(numbers)
    three_sum = set()
    for i in range(0, len_n - 2):
        for j in range(i + 1, len_n - 1):
            for k in range(j + 1, len_n):
                three_sum.add(numbers[i] + numbers[j] + numbers[k])
    result = sorted(three_sum, reverse=True)
    print('#{0} {1}'.format(test_case, result[4]))

# t = int(input())
 
# def go(idx, cnt, total, a, results):
#     if cnt == 3:
#         results.append(total)
#         return
#     if idx >= len(a):
#         return
#     go(idx+1, cnt, total, a, results)
#     go(idx+1, cnt+1, total+a[idx], a, results)
 
# for ti in range(1, t+1):
#     print(f'#{ti}', end=' ')
     
#     a = list(map(int, input().split()))
     
#     results = []
     
#     for i in range(len(a)):
#         go(i+1, 1, a[i], a, results)
     
#     res = sorted(list(set(results)))
     
#     print(res[-5])