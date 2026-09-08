class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        visited = set()
        for i in range(n):
            adj[i] = []

        for i in range(len(edges)):
            adj[edges[i][0]].append((succProb[i], edges[i][1]))
            adj[edges[i][1]].append((succProb[i], edges[i][0]))
        
        #we have an adjacency list with its neighhbours and the probability

        maxheap = [(-1, start_node)]
        visited.add((-1, start_node))
        
        while maxheap:
            p, n = heapq.heappop(maxheap)
            visited.add(n)

            if n == end_node:
                return -p

            for prob, neig in adj[n]:
                if neig not in visited:
                    heapq.heappush(maxheap, (prob * p, neig))
                
        return 0


        
        