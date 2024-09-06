class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:    
        for i in range(0, k):
            x = min(nums)
            x = x*multiplier
            y = nums.index(min(nums))
            nums[y] = x
        return nums
