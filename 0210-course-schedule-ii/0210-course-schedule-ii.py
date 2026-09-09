class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for c in range(numCourses):
            adj[c] = []
        for a, b in prerequisites:
            adj[a].append(b)
        visited = set()
        path = set()
        order = []
        def dfs(src, adj, prerequisites, visited, path):
            if src in path:
                return False
            if src in visited:
                return True
            
            visited.add(src)
            path.add(src)
            for neighbour in adj[src]:
                if dfs(neighbour, adj, prerequisites, visited, path) == False:
                    return False
            path.remove(src)
            order.append(src)
        
        for c in adj:
            if dfs(c, adj, prerequisites, visited, path) == False:
                return []
        return order