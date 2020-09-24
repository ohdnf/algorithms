from itertools import permutations

def is_prime(number):
    for k in range(2, int(number**(0.5))+1):
        if number % k == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    for r in range(1, len(numbers)+1):
        for number in permutations(numbers, r):
            curr = int(''.join(number))
            if is_prime(curr):
                # print(curr)
                answer.add(curr)
    answer -= {0, 1}
    return len(answer)


# 다른 사람의 풀이

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


if __name__ == "__main__":
    print(solution("17"), 3)
    print(solution("011"), 2)


"""
오답노트

dfs 접근, 모든 부분집합 찾기는 주어진 수의 순서를 바꿀 수 없어 불가능

"""