class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = []
        double = []
        for i in range(0, len(nums)):
            if nums[i] // 10 > 0:
                double.append(nums[i])
            else:
                single.append(nums[i])
        sum1 = 0
        for j in range(0, len(single)):
            sum1 = sum1 + single[j]
        sum2 = 0
        for k in range(0, len(double)):
            sum2 = sum2 + double[k]
        if sum1 == sum2:
            return False
        else:
            return True
        
