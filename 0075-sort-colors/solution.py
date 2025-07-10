class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for i in nums:
            if i == 0:
                counts[0] += 1
            if i == 1:
                counts[1] += 1
            if i == 2:
                counts[2] += 1
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1
            
