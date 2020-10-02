from collections import defaultdict, Counter
import re

def most_common_word(paragraph: str, banned) -> str:
    counts = defaultdict(int)
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).split() if word not in banned]
    for word in words:
        counts[word.lower()] += 1
    print(counts)
    return max(counts, key=counts.get)

if __name__ == "__main__":
    print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]), "ball")