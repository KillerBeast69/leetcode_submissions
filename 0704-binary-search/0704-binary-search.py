class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        
        return -1
        