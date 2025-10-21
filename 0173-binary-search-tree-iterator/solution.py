# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        stack = []
        self.arr = []
        cur = root
        self.i = 0
        while(cur or stack):
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                self.arr.append(cur.val)
                cur = cur.right


    def next(self) -> int:
        val = self.arr[self.i]
        self.i += 1
        return val


    def hasNext(self) -> bool:
        if self.i < len(self.arr):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
