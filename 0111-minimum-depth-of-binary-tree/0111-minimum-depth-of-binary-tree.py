# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, node):
        if not node:
            return 0
            
        # leftDepth = self.getDepth(node.left)
        # rightDepth = self.getDepth(node.right)

        if node.left is None and node.right is not None:
            # return 1 + rightDepth
            return 1 + self.getDepth(node.right)
        
        if node.right is None and node.left is not None:
            # return 1 + leftDepth
            return 1 + self.getDepth(node.left)
        
        return 1 + min(self.getDepth(node.left), self.getDepth(node.right))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
        