def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = money[0]
    
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
    
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
    
    return max(dp1[-2], dp1[-1], dp2[-1])


# 다른 사람의 풀이
def other_solution(money):
    x1, y1, z1 = money[0], money[1], money[0]+money[2]
    x2, y2, z2 = 0, money[1], money[2]
    for i in money[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)

if __name__ == "__main__":
    print(solution([1,2,3,1]), 4)

"""
오답 노트

dp의 각 원소를 [해당 집을 터는 경우, 안 터는 경우]로 구분했다.
하지만 이 경우 마지막 집을 털 때 첫 번째 집을 털었는지 여부를 알 수 없다.

첫 번째 집을 터는 경우와 안 터는 경우로 나눠서 생각해야 한다.
그리고 다른 사람의 풀이는 미쳤다 그냥
"""