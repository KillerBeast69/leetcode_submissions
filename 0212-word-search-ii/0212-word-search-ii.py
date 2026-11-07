class Node:
    def __init__(self):
        self.children = {}
        self.isword = False

    def addword(self, word):
        cur = self
        for i in word:
            if i not in cur.children:
                cur.children[i] = Node()
            cur = cur.children[i]
        
        cur.isword = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = Node()
        for w in words:
            root.addword(w)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] not in node.children or
                (r, c) in visited
            ):
                return

            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isword:
                res.add(word)
                node.isword = False
                
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)