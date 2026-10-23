class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = -1

        for i in range(len(nums)):
            if i == nums[i]:
                continue

            res &= nums[i]
        
        return res if res != -1 else 0