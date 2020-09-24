def solution(brown, yellow):
    b = -(brown // 2 + 2)
    ac = brown + yellow
    return [(-b + int( (b**2 - 4*ac)**0.5) )//2, (-b - int( (b**2 - 4*ac)**0.5 ) )//2]

# 다른 사람의 풀이
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))


"""
근의 공식으로 풀었다.

다른 사람의 풀이를 보고 든 생각은
해당 풀이에 달린 다른 사람의 댓글로 대신한다.
개같은 수학자놈들,,
"""