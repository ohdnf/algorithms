from typing import List

class Solution:
    # First solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * (n+1)
        right = [1] * (n+1)
        for idx in range(1, n+1):
            left[idx] = left[idx-1] * nums[idx-1]
            right[-idx-1] = right[-idx] * nums[-idx]
        result = [0] * n
        for idx in range(n):
            result[idx] = left[idx] * right[idx+1]
        return result
    
    # Two directions
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        for idx in range(len(nums)):
            result.append(product)
            product *= nums[idx]
        product = 1
        for idx in range(len(nums)-1, -1, -1):
            result[idx] *= product
            product *= nums[idx]
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]), [24,12,8,6])