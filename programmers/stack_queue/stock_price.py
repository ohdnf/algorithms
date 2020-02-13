def solution(prices):
    answer = []
    stack = [10000]
    min_stack = min_index = 0
    while prices:
        tail = prices.pop()
        if tail < stack[-1]:
            min_stack = tail
            min_index = 0
        else:
            min_index += 1
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))