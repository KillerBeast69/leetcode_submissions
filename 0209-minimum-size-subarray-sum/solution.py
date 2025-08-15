class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        length = inf
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                length = min(length, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if length == inf else length
            
