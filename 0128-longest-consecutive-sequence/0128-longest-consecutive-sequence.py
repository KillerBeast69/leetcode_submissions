class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        hashset = set(nums)

        cmax = 1
        for n in hashset:
            if n - 1 not in hashset:
                i = n
                c = 0
                while i in hashset:
                    i += 1
                    c += 1
                cmax = max(cmax, c)
        
        return cmax