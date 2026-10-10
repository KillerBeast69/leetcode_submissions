class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashset = set(nums)
        lmax = 0
        for i in hashset:
            if i - 1 not in hashset:
                l = 0
                while i in hashset:
                    l += 1
                    lmax = max(lmax, l)
                    i += 1
        
        return lmax