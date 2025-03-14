# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # define the ending condition of recursive
        if root is None:
            return root
        # each level function:
        if root.val < low:
            return self.trimBST(root.right,low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.right = self.trimBST(root.right,low, high)
            root.left = self.trimBST(root.left, low, high)
        return root

        