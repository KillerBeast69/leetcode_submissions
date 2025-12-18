class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxprofit = []
        mincapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(mincapital)

        for i in range(k):

            while mincapital and mincapital[0][0] <= w:
                c, p = heapq.heappop(mincapital)
                heapq.heappush(maxprofit, -p)

            if not maxprofit:
                break
            w += -1 * heapq.heappop(maxprofit)
        return w

