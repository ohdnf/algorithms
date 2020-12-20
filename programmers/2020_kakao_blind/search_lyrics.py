def solution(words, queries):
    answer = []
    # 가사 단어 길이별로 저장
    words_by_length = dict()
    for word in words:
        words_by_length[len(word)] = words_by_length.get(len(word), set()) | {word, }

    # 쿼리에 맞는 단어 검색
    for query in queries:
        count = 0
        length = len(query)
        same_length_words = words_by_length.get(length, set())
        # 쿼리와 길이가 같은 단어들과 비교
        for word in same_length_words:
            for i in range(length):
                if query[i].isalpha():
                    if query[i] != word[i]:
                        break
                else:
                    continue
            else:
                count += 1
        answer.append(count)
    return answer


if __name__ == "__main__":
    w = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    q = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(w, q))