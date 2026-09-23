class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        hashmap = {}

        def helper(total, index):
            if index >= len(nums):
                if total == target:
                    return 1
                return 0

            if (total, index) in hashmap:
                return hashmap[(total, index)]
            
            branch_sum = helper(total + nums[index], index + 1) + helper(total - nums[index], index + 1)

            #now what should I store in hashmap??
            hashmap[(total, index)] = branch_sum

            return branch_sum
        
        return helper(0, 0)


        