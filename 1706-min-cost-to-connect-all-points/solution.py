class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minheap = []

        for neighbour in range(len(points)):
            cost = abs(points[neighbour][0] - points[0][0]) + abs(points[neighbour][1] - points[0][1])
            heapq.heappush(minheap, (cost, 0, neighbour))
        
        total = 0
        visited.add(0)
        while len(visited) < len(points):
            weight, n1, n2 = heapq.heappop(minheap)
            if n2 in visited:
                continue
            total += weight
            visited.add(n2)
            for neighbour in range(len(points)):
                if neighbour not in visited:
                    cost = abs(points[neighbour][0] - points[n2][0]) + abs(points[neighbour][1] - points[n2][1])
                    heapq.heappush(minheap, (cost, n2, neighbour))
        return total

        
        


