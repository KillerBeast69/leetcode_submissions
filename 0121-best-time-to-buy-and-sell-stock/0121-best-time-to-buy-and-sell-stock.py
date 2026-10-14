class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        tot, i, j = 0, 0, 0
        n = len(prices)
        while i <= j < n:
            pro = prices[j] - prices[i]
            if pro <= 0:
                i = j
            else:
                tot = max(tot, pro)
            j += 1

        return tot

