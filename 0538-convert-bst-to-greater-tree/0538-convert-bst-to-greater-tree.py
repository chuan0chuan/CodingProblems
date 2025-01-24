# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # define the para and return of travesal funtion:
    def travesal(self,root):
        if root is None:
            return root
        self.travesal(root.right)
        root.val += self.pre
        # forgot to move point
        self.pre = root.val
        self.travesal(root.left)

    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0
        self.travesal(root)
        return root