def reorderLogFiles(logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    letter_logs = []
    digit_logs = []

    for log in logs:
        identifier, *words = log.split()
        if words[0].isdigit():
            digit_logs.append(log)
            continue
        letter_logs.append([identifier, words])

    letter_logs.sort(key=lambda log: ('0'.join(log[1]), log[0]))
    letter_logs = [identifier + ' ' + ' '.join(words) for identifier, words in letter_logs]
    return letter_logs+digit_logs

if __name__ == "__main__":
    # print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
    # print(reorderLogFiles(["g1 act car","a2 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]))
    print(reorderLogFiles(["j mo", "5 m w", "g 07", "o 2 0", "t q h"]), ["5 m w","j mo","t q h","g 07","o 2 0"], sep='\n')