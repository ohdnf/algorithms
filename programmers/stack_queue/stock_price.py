def solution(prices):
    answer = [0]
    # 떨어지는 가격, 그 가격부터 증가하는 구간의 길이
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


# 강사님 풀이
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    answer.append(0)

# 태우님 풀이
def solution(prices):
    stack = []
    result = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            x = stack.pop()
            result[x] = i - x
        stack.append(i)
    while stack:
        x = stack.pop()
        result[x] = i - x
    return result


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))