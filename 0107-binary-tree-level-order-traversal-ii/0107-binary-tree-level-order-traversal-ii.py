# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #1. define the parameter and return value 
    def travesal(self, node: Optional[TreeNode], level:int, levels:List[List[int]]):
        # 2. the ending condition to jump out
        if node is None:
            return node
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.val)
        self.travesal(node.left, level+1, levels)
        self.travesal(node.right, level+1, levels)
    
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        self.travesal(root, 0 , levels)
        levels.reverse()
        return levels