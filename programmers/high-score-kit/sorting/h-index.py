def solution(citations):
    """
    H-index:
    발표한 논문 n편 중, 
    h번 이상 인용된 논문이 h편 이상이고 
    나머지 논문이 h번 이하 인용되었을 때
    이 둘을 동시에 만족하는 h의 최댓값
    """
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        """
        인용 수를 내림차순으로 정렬했으므로
        `citations[i]`번 이상 인용된 논문은 `i+1`편 존재한다.
        h-index는 `citations[i] >= i+1`인 조건에서 최대값이므로
        `i+1 > citation[i]`인 경우 반복문을 종료한다.
        """
        if i+1 > citations[i]:
            break
        answer += 1
    
    return answer


if __name__ == "__main__":
    solution([3, 0, 6, 1, 5])