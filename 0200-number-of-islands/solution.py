class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        total = 0

        def bfs(r, c):
            q = deque([])
            visited.add((r,c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                    c in range(columns) and
                    grid[r][c] != "0" and
                    ((r, c)) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    total += 1
        return total
