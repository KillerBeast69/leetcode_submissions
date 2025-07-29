class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns, maximum = len(grid), len(grid[0]), 0
        visited = set()

        def bfs(r, c):
            total = 0
            q = deque([])
            visited.add((r, c))
            q.append((r, c))
            count = 1
            while q:
                rw, cl = q.popleft()
                directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = rw + dr, cl + dc
                    if (r in range(rows) and
                    c in range(columns) and
                    grid[r][c] != 0 and
                    ((r, c)) not in visited):
                        count += 1
                        q.append((r, c))
                        visited.add((r, c))
            print(count)
            return count

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    temp = bfs(r, c)
                    if temp > maximum:
                        maximum = temp
        return maximum

                
                    
