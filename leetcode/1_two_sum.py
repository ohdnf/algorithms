from typing import List

# brute-force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# using `in` operation
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            remaining = target - num
            if remaining in nums[idx+1:]:
                return [idx, nums.index(remaining)]


# one-pass hash table
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([-1,-2,-3,-4,-5], -8), [2, 4])