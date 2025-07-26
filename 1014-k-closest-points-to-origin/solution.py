import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for x, y in points:
            total = self.formula(x, y)
            dis.append([total, x, y])
        heapq.heapify(dis)
        res = []
        while k > 0:
            total, x, y = heapq.heappop(dis)
            res.append([x, y])
            k -= 1
        return res
             

    def formula(self, p1, p2):
        return (p1 * p1) + (p2 * p2)
        
