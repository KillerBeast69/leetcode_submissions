class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        total = 0
        c = 0
        while(l < r):
            if lmax <= rmax:
                l += 1
                cur = min(lmax, rmax) - height[l]
                if height[l] > lmax:
                    lmax = height[l]
            else:
                r -= 1
                cur = min(lmax, rmax) - height[r]
                if height[r] > rmax:
                    rmax = height[r]
            if cur > -1:
                total += cur
        return total
