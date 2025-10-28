class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small, large = [], []
        d = defaultdict(int)

        for i in range(k):
            heapq.heappush(small, -nums[i])
        for i in range(k // 2):
            heapq.heappush(large, -heapq.heappop(small))

        res = [-small[0] if k & 1 else (large[0] - small[0]) / 2]
        for i in range(k, len(nums)):
            d[nums[i - k]] += 1
            balance = -1 if small and nums[i - k] <= -small[0] else 1

            if small and nums[i] <= -small[0]:
                heapq.heappush(small, -nums[i])
                balance += 1
            else:
                heapq.heappush(large, nums[i])
                balance -= 1

            if balance > 0:
                heapq.heappush(large, -heapq.heappop(small))
            if balance < 0:
                heapq.heappush(small, -heapq.heappop(large))

            while small and d[-small[0]] > 0:
                d[-heapq.heappop(small)] -= 1

            while large and d[large[0]] > 0:
                d[heapq.heappop(large)] -= 1

            res.append(-small[0] if k & 1 else (large[0] - small[0]) / 2)

        return res