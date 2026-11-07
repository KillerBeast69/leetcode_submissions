class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                i >= len(word) or
                word[i] != board[r][c]
            ):
                return False

            visited.add((r, c))
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            visited.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                        return True

        return False
            