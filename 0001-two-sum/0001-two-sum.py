class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashmap:
                return [i, hashmap[val]]
            hashmap[nums[i]] = i
        