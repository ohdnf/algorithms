from typing import List
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            c = Counter(word)
            key = ''.join(sorted(c.elements()))
            anagram = group.get(key, [])
            anagram.append(word)
            group[key] = anagram
        return [anagrams for anagrams in group.values()]

# categorize by sorted string
class Solution(object):
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

# categorize by count
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

if __name__ == "__main__":
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat","abandon","donanba","badonan"]
    print(s.groupAnagrams(strs), [["bat"],["nat","tan"],["ate","eat","tea"]])