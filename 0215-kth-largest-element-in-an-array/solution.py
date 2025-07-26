class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        dif = abs(k - len(nums))
        heapq.heapify(nums)
        while (dif > 0):
            heapq.heappop(nums)
            dif -= 1
        return heapq.heappop(nums)

        
