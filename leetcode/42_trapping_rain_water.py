from typing import List

class Solution:
    # def trap(self, height: List[int]) -> int:
    #     if len(height) < 3:
    #         return 0
    #     water = 0
    #     peak_height = max(height)
    #     peak_index = height.index(peak_height)
    #     small_peak = height[0]
    #     for idx in range(1, peak_index):
    #         if height[idx] >= small_peak:
    #             small_peak = height[idx]
    #         else:
    #             water += small_peak - height[idx]
    #     small_peak = height[-1]
    #     for idx in range(len(height)-2, peak_index, -1):
    #         if height[idx] >= small_peak:
    #             small_peak = height[idx]
    #         else:
    #             water += small_peak - height[idx]
        
    #     return water

    # 투 포인터를 최대로 이동
    # def trap(self, height: List[int]) -> int:
    #     if not height:
    #         return 0
        
    #     volume = 0
    #     left, right = 0, len(height) - 1
    #     left_max, right_max = height[left], height[right]

    #     while left < right:
    #         left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
    #         # 더 높은 쪽을 향해 투 포인터 이동
    #         if left_max <= right_max:
    #             volume += left_max - height[left]
    #             left += 1
    #         else:
    #             volume += right_max - height[right]
    #             right -= 1
    #     return volume
    
    # 스택 쌓기
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            print(f'i: {i} height[i]: {height[i]}')
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()
                print('stack:', stack)
                print('top:', top)
                if not stack:
                    break
                
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                print(f'distance = {i} - {stack[-1]} - 1 = {distance}')
                waters = min(height[i], height[stack[-1]]) - height[top]
                print(f'waters = {min(height[i], height[stack[-1]])} - {height[top]} = {waters}')
                volume += distance * waters
                print(f'volume += {distance * waters}')
            
            stack.append(i)
            print('stack.append(i) ==>', stack)
            print('volume:', volume)
            print()
        return volume

if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
