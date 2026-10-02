class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []
        pre = 1

        for i in range(len(nums)):
            output.append(pre)
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post
            post *= nums[i]
        
        return output