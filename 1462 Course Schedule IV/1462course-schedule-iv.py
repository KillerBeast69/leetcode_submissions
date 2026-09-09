class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for c in range(numCourses):
            adj[c] = []
        
        for a, b in prerequisites:
            adj[a].append(b)
        
        pre = {}
        for i in range(numCourses):
            pre[i] = set()

        for i in range(numCourses):
            q = deque()
            visited = set()
            q.append(i)
            while q:
                cur = q.popleft()
                for neighbour in adj[cur]:
                    pre[neighbour].add(i)
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append(neighbour)
        
        res = []
        for u, v in queries:
            if u in pre[v]:
                res.append(True)
            else:
                res.append(False)
        
        return res