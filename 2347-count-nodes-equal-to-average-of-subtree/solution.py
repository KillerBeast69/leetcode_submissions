# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        #first we need to construct a tree?
        #children of node i are i + 1 and i + 2
        #wait is the tree already constructed?
        #because the root is of treenode
        count = 0
        def dfs(node):
            nonlocal count
            total = node.val
            n = 1
            if node.left == None and node.right == None:
                count += 1
                return (node.val, n)
        
            if node.left:
                l_total, l_n = dfs(node.left)
                total += l_total
                n += l_n
            if node.right:
                r_total, r_n = dfs(node.right)
                total += r_total
                n += r_n
            
            average = total // n
            if average == node.val:
                count += 1
            return (total, n)

        dfs(root)
        return count
