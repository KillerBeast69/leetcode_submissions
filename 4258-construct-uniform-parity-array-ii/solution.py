class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        iseven = True
        even = float('inf')
        odd = float('inf')
        for i in nums1:
            if i % 2 == 0 and i < even:
                even = i
            if i % 2 != 0 and i < odd:
                odd = i
                iseven = False
        #now we have the smallest odd and even numbers
        if iseven:
            return True
        if even - odd >= 1:
            return True
        return False
