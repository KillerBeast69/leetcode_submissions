class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for s, d, w in times:
            adj[s].append([d, w])

        minheap = [[0, k]]

        shortest = {}
        maxi = -1

        while minheap:
            w1, n1 = heapq.heappop(minheap)

            if n1 in shortest:
                continue
            
            shortest[n1] = w1
            
            maxi = max(maxi, w1)

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [w2 + w1, n2])
            
            
        if len(shortest) != n:
            return -1
        return maxi
        
