class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        table = set(nums)
        maxi = 0
        for i in table:
            if (i - 1) not in table:
                count = 1
                j = i + 1
                while(j in table):
                    count += 1
                    j += 1
                maxi = max(maxi, count)
        return maxi
