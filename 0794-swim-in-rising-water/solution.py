class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap = [[grid[0][0], 0, 0]]
        visited = set()

        visited.add((0, 0))

        ROWS = len(grid)
        COLS = len(grid[0])

        while minheap:
            t, r, c = heapq.heappop(minheap)

            if r == ROWS - 1 and c == COLS - 1:
                return t
            
            neighbours = [[0,1], [1,0], [-1,0], [0,-1]]

            for x, y in neighbours:
                xr = x + r
                yc = y + c

                if 0 <= xr < ROWS and 0 <= yc < COLS and (xr, yc) not in visited:
                    visited.add((xr, yc))

                    max_time = max(t, grid[xr][yc])

                    heapq.heappush(minheap, (max_time, xr, yc))


