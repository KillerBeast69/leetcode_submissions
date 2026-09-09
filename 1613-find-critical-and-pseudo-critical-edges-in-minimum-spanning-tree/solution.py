class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.edges_added = 0
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
    
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.edges_added += 1
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #how do I loop through newly sorted edges??
        #how do I sort edges based on its weight?
        #maybe create a minheap??
        my_array = []
        for index, (a, b, w) in enumerate(edges):
            my_array.append([w, a, b, index])
        
        my_array.sort()

        uf = UnionFind(n)
        base_weight = 0
        #maybe I should sort the edges in reverse order?
        #because popping from heap is log n and popping from array is constant
        #but how do I sort the array based on the weight
        j = 0
        for weight, n1, n2, i in my_array:
            #instead of popping the array I could just shift the index to left

            if not uf.union(n1, n2):
                continue
            base_weight += weight
        #now we have base weight
 
        #now the what if phase
        #creating fresh union find
        crit = []
        p_crit = []
        for e in range(len(edges)):
            uf0 = UnionFind(n)
            total = 0
            #we are testing for edge e
            #conduct kruskal without adding this edge
            for weight, n1, n2, i in my_array:
                if i != e:
                    if not uf0.union(n1, n2):
                        continue
                    total += weight
            #we get total when we do not include edge e
            #if the total is greater than base weight or 
            if total > base_weight or uf0.edges_added < n - 1:
                crit.append(e)
                continue
            n1, n2, weight = edges[e]
            total = 0
            uf1 = UnionFind(n)
            uf1.union(n1, n2)
            total += weight
            for weight, n1, n2, i in my_array:
                if not uf1.union(n1, n2):
                    continue
                total += weight
            if total == base_weight:
                p_crit.append(e)
        
        return [crit, p_crit]
            
                
