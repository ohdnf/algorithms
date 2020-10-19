from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(s)

        for letter in s:
            counter[letter] -= 1
            if letter in stack:
                continue
            while stack and letter < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(letter)

        return ''.join(stack)

    # 재귀
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters("bcabc"), "abc")
    print(sol.removeDuplicateLetters("cbacdcbc"), "acdb")
