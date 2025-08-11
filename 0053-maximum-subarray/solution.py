class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -inf
        cursum = -inf
        for n in nums:
            cursum = max(cursum, 0)
            cursum += n
            maxsum = max(maxsum, cursum)
        return maxsum
