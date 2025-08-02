"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldnew = {}   
        def dfs(cur):
            if cur in oldnew:
                return oldnew[cur]
            copy = Node(cur.val)
            oldnew[cur] = copy
            for neighbor in cur.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None

        
