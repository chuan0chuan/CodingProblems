# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (not root2 and root1):
            return False
        Tree1Levels = []
        Tree2Levels = []
        def traverse(node, level, Levels):
            if not node:
                return
            if len(Levels) == level:
                Levels.append([])
            Levels[level].append(node.val)
            traverse(node.left, level + 1, Levels)
            traverse(node.right, level + 1, Levels)

        traverse(root1, 0 , Tree1Levels)
        traverse(root2, 0 , Tree2Levels)
        if len(Tree1Levels) != len(Tree2Levels):
            return False
        for i in range(len(Tree1Levels)):
            if Counter(Tree1Levels[i]) != Counter(Tree2Levels[i]):
                return False
        return True

 
        
        
