class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele = 0
        dig = 0
        for i in range(0, len(nums)):
            ele = ele + nums[i]
            temp = nums[i]
            while(temp>0):
                sum = temp % 10
                dig = dig + sum
                temp = temp // 10
        absolute = abs(ele - dig)
        return absolute
                


