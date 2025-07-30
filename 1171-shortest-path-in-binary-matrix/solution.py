class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        q = deque()
        visited = set()
        q.append((0, 0))
        visited.add((0,0))
        length = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r == rows - 1 and c == columns - 1):
                    return length
                
                neighbours = [[0, -1], [0, 1], [1, 0], [-1, 0], [1, -1], [1, 1], [-1, -1], [-1, 1]]
                for dr, dc in neighbours:
                    R, C = dr + r, dc + c
                    if (min(R, C) < 0 or 
                    R >= rows or C >= columns or 
                    (R, C) in visited or 
                    grid[R][C] == 1):
                        continue
                    q.append((R, C))
                    visited.add((R, C))
            length += 1
        return -1
            
