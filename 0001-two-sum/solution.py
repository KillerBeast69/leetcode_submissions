class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = None
        table = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in table:
                return [table[dif], i]
            else:
                table[nums[i]] = i
        
