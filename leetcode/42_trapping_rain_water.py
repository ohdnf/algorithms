class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        water = 0
        peak_height = max(height)
        peak_index = height.index(peak_height)
        small_peak = height[0]
        for idx in range(1, peak_index):
            if height[idx] >= small_peak:
                small_peak = height[idx]
            else:
                water += small_peak - height[idx]
        small_peak = height[-1]
        for idx in range(len(height)-2, peak_index, -1):
            if height[idx] >= small_peak:
                small_peak = height[idx]
            else:
                water += small_peak - height[idx]
        
        return water