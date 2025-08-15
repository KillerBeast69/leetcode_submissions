class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxw = 0
        l = 0
        r = len(height) - 1
        while(l < r):
            vol = min(height[l], height[r]) * (r - l)
            maxw = max(maxw, vol)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxw
