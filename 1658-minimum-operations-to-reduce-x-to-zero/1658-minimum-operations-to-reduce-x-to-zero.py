class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1
        
        if target == 0:
            return len(nums)

        maxl = -1
        left = 0
        cur = 0

        for right in range(len(nums)):
            cur += nums[right]

            while cur > target and left <= right:
                cur -= nums[left]
                left += 1
            
            if cur == target:
                maxl = max(maxl, right - left + 1)
            
        return len(nums) - maxl if maxl != -1 else -1