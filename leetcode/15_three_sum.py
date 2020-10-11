from itertools import combinations
from typing import List

class Solution:
    # Brute Force
    def threeSum_bf(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        
        for i in range(len(nums)-2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.append([nums[i], nums[j], nums[k]])
        return triplets

    # Two Pointers
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                three = nums[i] + nums[left] + nums[right]
                if three < 0:
                    left += 1
                elif three > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return triplets

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
    print(solution.threeSum([]), [])
    print(solution.threeSum([13,-4,1,3,-1,-1,5,-11,13,9,4,7,5,-5,-13,-4,8,-3,14,-4,14,6,7,11,4,-6,-5,-9,14,3,-9,12,-15,0,-8,-9,14,4,-5,4,-1,-15,-12,-11,-13,-9,1,3,-5,0,14,-6,13,-1,12,2,8,-7,9,0,11,7,-11,3,-8,-11,1,13,8,4,-5,14,4,-2,11,-2,-4,-3,-14,6,4,8,7,3,-8,5,12,7,5,-2,-8,-7,13,-11,12,12,-7,-10,11,-14]), [])
    print(solution.threeSum([0]), [])


"""
투 포인터(Two pointers) 기법
- 시작점(왼쪽)과 끝점(오른쪽), 두 지점을 기준으로 범위를 좁혀나가는 문제 풀이 전략
- 주로 정렬된 배열에서 사용
"""