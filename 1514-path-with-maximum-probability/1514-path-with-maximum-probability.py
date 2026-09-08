class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        max_prob = [0.0] * n
        for i in range(n):
            adj[i] = []

        for i in range(len(edges)):
            adj[edges[i][0]].append((succProb[i], edges[i][1]))
            adj[edges[i][1]].append((succProb[i], edges[i][0]))
        
        #we have an adjacency list with its neighhbours and the probability

        maxheap = [(-1, start_node)]
        
        while maxheap:
            p, node = heapq.heappop(maxheap)

            if node == end_node:
                return -p

            for prob, neig in adj[node]:
                new_prob = -p * prob
                if new_prob > max_prob[neig]:
                    max_prob[neig] = new_prob
                    heapq.heappush(maxheap, (prob * p, neig))
                    
                
        return 0


        
        