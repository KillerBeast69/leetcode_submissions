class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        vmax = 0
        while i < j:
            vmax = max(vmax, (min(height[i], height[j]) * (j - i)))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return vmax
