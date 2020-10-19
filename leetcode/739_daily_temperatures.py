from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0] * len(T)
        for idx, curr in enumerate(T):
            while stack and curr > T[stack[-1]]:
                last = stack.pop()
                result[last] = idx - last
            stack.append(idx)
        return result


"""
42. 빗물 트래핑과 유사한 문제
for idx, temp in enumerate(T) 할 필요없이, 인덱스만 스택에 쌓는다.
"""