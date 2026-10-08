class Solution:
    def trap(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        lmax, rmax, res = height[i], height[j], 0

        while i < j:
            if lmax < rmax:
                i += 1
                lmax = max(lmax, height[i])
                res += lmax - height[i]
            else:
                j -= 1
                rmax = max(rmax, height[j])
                res += rmax - height[j]

        return res
        