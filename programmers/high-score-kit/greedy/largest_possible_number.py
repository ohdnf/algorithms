from collections import deque as dq

def solution(number, k):
    answer = []
    final_len = len(number) - k
    number = dq(map(int, list(number)))
    count = 0
    while count < k and number:
        curr = number.popleft()
        while answer and answer[-1] < curr and count < k:
            answer.pop()
            count += 1
        answer.append(curr)
        # print(answer, number, curr, count, k)
    more = final_len - len(answer)
    # print(number, answer, count, final_len, more)
    if more > 0:
        number = list(number)
        answer.extend(number[:more])
    elif more < 0:
        for _ in range(-more):
            answer.pop()
    return ''.join(map(str, answer))


def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


if __name__ == "__main__":
    print(solution("1924", 2))
    print(solution("1231234", 3))
    print(solution("4177252841", 4))
    print(solution("1234567890", 1))
    print(solution("1234567890", 9))
    print(solution("123456789", 1))
    print(solution("123456789", 8))
    print(solution("9876543210", 1))
    print(solution("9876543210", 9))
    print(solution("987654321", 1))
    print(solution("987654321", 8))