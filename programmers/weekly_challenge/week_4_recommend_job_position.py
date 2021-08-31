from collections import defaultdict

def solution(table, languages, preference):
    calc = defaultdict(int)
    new_table = {}
    for row in table:
        position, five, four, three, two, one = row.split()
        new_table[position] = {
            five: 5,
            four: 4,
            three: 3,
            two: 2,
            one: 1
        }
    for idx in range(len(languages)):
        cur_lang = languages[idx]
        cur_pref = preference[idx]
        for position in new_table:
            if cur_lang in new_table[position]:
                calc[position] += new_table[position][cur_lang] * cur_pref
    result = [(key, val) for key, val in calc.items()]
    result.sort(key=lambda item: (-item[1], item[0]))
    return result[0][0]

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.1MB)
"""
