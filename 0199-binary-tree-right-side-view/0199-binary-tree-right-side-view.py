# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travesal(self, node: Optional[TreeNode], level: int, levels: List[List[int]]):
        if node is None:
            return node
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.val)
        self.travesal(node.left, level + 1, levels)
        self.travesal(node.right, level + 1, levels)

    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # order travesal firstly
        levels = []
        self.travesal(root, 0, levels)
        return [level[-1] for level in levels]
