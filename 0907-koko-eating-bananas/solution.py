import math
class Solution:
    def iskCorrect(self, k, h, piles):
        total = 0
        print(k)
        for i in piles:
            total = math.ceil(i / k) + total
        print("total = ", total)
        if total > h:
            return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 0
        k = 0
        final = None
        for i in piles:
            if i > r:
                r = i
        while (l <= r):
            k = (l + r) // 2
            if self.iskCorrect(k, h, piles):
                r = k - 1
                final = k
            else:
                l = k + 1
        return final

