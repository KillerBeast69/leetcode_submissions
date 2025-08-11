class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        minsum = 0
        globalmin = nums[0]
        maxsum = 0
        globalmax = nums[0]
        for n in nums:
            total += n
            minsum = min(minsum, 0)
            maxsum = max(maxsum, 0)
            minsum += n
            maxsum += n
            globalmax = max(globalmax, maxsum)
            globalmin = min(globalmin, minsum)
        if globalmax < 0:
            return globalmax
        return max(globalmax, total - (globalmin))
