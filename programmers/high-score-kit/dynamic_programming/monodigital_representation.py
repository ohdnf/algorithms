def solution(N, number):
    if number == N:
        return 1
    
    dp = {1: {N,}}
    for cnt in range(2, 9):
        dp[cnt] = set()
        dp[cnt].add(int(str(N)*cnt))
        for i in range(1, cnt):
            for num1 in dp[i]:
                for num2 in dp[cnt-i]:
                    if num1+num2 < 32001: dp[cnt].add(num1+num2)
                    if num1-num2 > 0: dp[cnt].add(num1-num2)
                    if num2-num1 > 0: dp[cnt].add(num2-num1)
                    if num1//num2 > 0: dp[cnt].add(num1//num2)
                    if num2//num1 > 0: dp[cnt].add(num2//num1)
                    if num1*num2 < 32001: dp[cnt].add(num1*num2)
        print(cnt, dp[cnt])
        if number in dp[cnt]:
            return cnt
    
    return -1


if __name__ == "__main__":
    # print(solution(5, 12), 4)
    # print(solution(2, 11), 3)
    # print(solution(1, 11), 2)
    print(solution(1, 100), 5)


"""
오답 노트

1. 조건을 잘 보자!

조건을 보면 return 값은 범위가 8까지(이상이면 -1 반환), number는 범위가 32000까지이다.
DP를 하더라도 number로 하게 되면 시간이 오래 걸린다.

2. 접근 방법 생각하기

때문에 N을 하나 더 사용했을 때 구할 수 있는 값을 차례로 계산하는 것이 가장 좋은 방법이다.

count   |   value
1       |   N
2       |   NN, N+N, N-N, N*N, N//N
3       |   NNN, count(1) & count(2), count(2) & count(1)
4       |   NNNN, count(1) & count(3), count(2) & count(2), count(3) & count(1)
...
k       |   N...N(k), count(1) & count(k-1), count(2) & count(k-2), ... count(k-1) & count(1)

&: count(i)의 각 원소와 count(j)의 각 원소의 사칙연산
"""