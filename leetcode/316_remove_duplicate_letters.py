from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = collections.Counter(s)

        for letter in s:
            counter[letter] -= 1
            if letter in stack:
                continue
            while stack and letter < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(letter)

        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicateLetters("bcabc"), "abc")
    print(s.removeDuplicateLetters("cbacdcbc"), "acdb")
