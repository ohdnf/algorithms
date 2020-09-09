def solution(relation):
    attrs = list(zip(*relation))
    # print(attrs)
    col_length = len(relation[0])
    rel_length = len(relation)

    candidates = []

    # 속성의 모든 부분 집합
    for i in range(1<<col_length):
        new = [j for j in range(col_length+1) if i & (1<<j)]
        # print(candiadate)
        # 현재 키가 후보키를 포함하는지 최소성 검사
        for candidate in candidates:
            if set(candidate) <= set(new):
                break
        else:
            # 현재 키가 모든 튜플을 식별할 수 있는지 유일성 검사
            check = set(zip(*[attrs[i] for i in new]))
            if len(check) == rel_length:
                candidates.append(new)
    return len(candidates)

if __name__ == "__main__":
    table = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(table))
