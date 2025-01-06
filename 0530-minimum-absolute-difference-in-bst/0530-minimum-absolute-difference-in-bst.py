# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def _init_(self):
        self.vec =[]
    
    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.left)
        self.vec.append(root.val)
        self.traversal(root.right)
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.vec=[]
        self.traversal(root)
        min_diff = float('inf')

        for i in range(1,len(self.vec)):
            diff = self.vec[i]- self.vec[i-1]
            min_diff = min(diff, min_diff)

        return min_diff