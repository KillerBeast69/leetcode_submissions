class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        #using a decision tree, first we need to find the target, the target has to be half the sum of all elements. will that lead to tle?
        total_sum = sum(nums)
        #what if the total sum is odd? how can there be two subsets such that their sum is same??

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        hashmap = {}

        def helper(total, index):
            if total > target:
                return False
            
            if index >= len(nums) or total > target:
                #this means we have reached the end of array and still have not found the subset??
                return False

            if (total, index) in hashmap:
                return hashmap[(total, index)]
            
            #what could be other base cases? I guess we must traverse now
            if total + nums[index] == target:
                return True

            res = helper(total, index + 1) or helper(total + nums[index], index + 1)

            hashmap[(total, index)] = res

            return res
        
        return helper(0, 0)