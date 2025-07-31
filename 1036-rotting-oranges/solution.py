class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        rows, columns = len(grid), len(grid[0])
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    q.append([row, column])
                if grid[row][column] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = -1
        while q:
            for i in range(len(q)):
                R, C = q.popleft()
                adjacent = [[0, -1], [0, 1], [1, 0], [-1, 0]]
                for dr, dc in adjacent:
                    r, c = R + dr, C + dc
                    if (min(r, c) < 0 or
                    r >= len(grid) or
                    c >= len(grid[0]) or
                    grid[r][c] == 2 or
                    grid[r][c] == 0):
                        continue
                    q.append((r, c))
                    grid[r][c] = 2
                    fresh -= 1
            minutes += 1
        print(fresh)
        if fresh == 0:
            return minutes
        return -1
        
                

