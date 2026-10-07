class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float('inf')

        def rate(r):
            hours = 0
            for i in piles:
                hours += (i + r - 1) // r
            
            return hours

        while l <= r:
            m = (l + r) // 2

            hours = rate(m)
            if hours <= h:
                r = m - 1
                res = min(res, m)
            elif hours > h:
                l = m + 1
            
        return res