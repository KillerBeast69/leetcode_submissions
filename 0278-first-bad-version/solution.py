# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        first = None
        while (l <= r):
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
                first = mid
            elif not isBadVersion(mid):
                l = mid + 1
        return first
