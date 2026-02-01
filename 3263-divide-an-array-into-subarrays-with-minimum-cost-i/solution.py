class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]
        min1 = inf
        min2 = inf
        for i in range(1, len(nums)):
            if nums[i] < min1:
                min1 = nums[i]
                if min1 < min2:
                    temp = min2
                    min2 = min1
                    min1 = temp
        return cost + min1 + min2
