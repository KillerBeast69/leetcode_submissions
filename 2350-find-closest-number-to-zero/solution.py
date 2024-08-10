class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        a = nums[0]
        n = len(nums)
        for i in range (0, n, 1):
            if (abs(nums[i])<abs(a)):
                a = nums[i]
            elif (abs(nums[i]) == abs(a)):
                a = max(a,nums[i])
        return a
