class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-s for s in stones]
        heapq.heapify(arr)
        print(arr)
        while(len(arr) > 1):
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            if second > first:
                heapq.heappush(arr, first - second)

        arr.append(0)
        return abs(arr[0])

        
