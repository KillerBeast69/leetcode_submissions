class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1

        vmax = 0
        while i < j:
            h = min(height[i], height[j])
            v = h * (j - i)
            vmax = max(vmax, v)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return vmax