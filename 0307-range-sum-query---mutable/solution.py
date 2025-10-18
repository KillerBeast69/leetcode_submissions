class SegmentTreeNode:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R
    
    @staticmethod
    def build(nums, L, R):
        # Base case: single element
        if L == R:
            return SegmentTreeNode(nums[L], L, R)
        
        # Split the range in half
        M = (L + R) // 2
        root = SegmentTreeNode(0, L, R)
        
        # Build left and right subtrees
        root.left = SegmentTreeNode.build(nums, L, M)
        root.right = SegmentTreeNode.build(nums, M + 1, R)
        
        # Sum of this node = sum of children
        root.sum = root.left.sum + root.right.sum
        return root

class NumArray:
    def __init__(self, nums):
        # IMPORTANT: Save the root of the tree!
        self.root = SegmentTreeNode.build(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        # Helper function that works on a node
        def _update(node, index, val):
            # Found the leaf node to update
            if node.L == node.R:
                node.sum = val
                return
            
            # Decide which subtree contains the index
            M = (node.L + node.R) // 2
            if index > M:
                _update(node.right, index, val)
            else:
                _update(node.left, index, val)
            
            # Update sum after updating child
            node.sum = node.left.sum + node.right.sum
        
        _update(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        # Helper function that works on a node
        def _query(node, left, right):
            # This node's range is exactly what we need
            if left == node.L and right == node.R:
                return node.sum
            
            M = (node.L + node.R) // 2
            
            # Query range is entirely in right subtree
            if left > M:
                return _query(node.right, left, right)
            # Query range is entirely in left subtree
            elif right <= M:
                return _query(node.left, left, right)
            # Query range spans both subtrees
            else:
                return (_query(node.left, left, M) +
                        _query(node.right, M + 1, right))
        
        return _query(self.root, left, right)


# Example usage:
# nums = [1, 3, 5, 7, 9, 11]
# obj = NumArray(nums)
# print(obj.sumRange(1, 3))  # Sum of elements from index 1 to 3
# obj.update(1, 10)          # Update index 1 to value 10
# print(obj.sumRange(1, 3))  # Sum after update
