class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        k = 0
        c = 1
        p = 0
        for i in range(0, len(nums)):
            c = i + 1
            if c >= len(nums):
                nums[p] = nums[i]
                k = k + 1
                break
            if nums[i] != nums[c]:
                nums[p] = nums[i]
                p = p + 1
                k = k + 1
        print(k)
        return k
        
                


            

