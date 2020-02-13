def solution(prices):
    answer = [0]
    stack = [[prices.pop(), 0]]
    while prices:
        last = prices.pop()
        n = 1
        while stack and stack[-1][0] >= last:
            _, l = stack.pop()
            n += l
        stack.append([last, n])
        answer.append(n)
    return answer[::-1]

# def solution(prices):
#     answer = []
#     for i in range(len(prices)-1):
#         head = prices[i]
#         tail = prices[i+1:]
#         cnt = 0
#         for price in tail:
#             cnt += 1
#             if head > price:
#                 break
#         answer.append(cnt)
#     answer.append(0)
#     return answer


# def solution(prices):
#     answer = []
#     n = len(prices)
#     while n > 1:
#         cnt = 0
#         head = prices.pop(0)
#         for price in prices:
#             cnt += 1
#             if head > price:
#                 break
#         answer.append(cnt)
#         n -= 1
#     answer.append(0)
#     return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))