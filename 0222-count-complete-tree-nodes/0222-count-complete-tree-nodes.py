# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.getNodesNum(root)

    def getNodesNum(self, node) -> int:
        if not node:
            return 0

        leftNum = self.countNodes(node.left)
        rigthNum = self.countNodes(node.right)
        return 1+ leftNum + rigthNum