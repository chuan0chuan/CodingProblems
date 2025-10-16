# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, path = [], []

        def dfs(node, remain):
            if not node:
                return 
            
            path.append(node.val)

            if not node.left and not node.right and remain == node.val:
                res.append(path[:])
            else:
                dfs(node.left, remain - node.val)
                dfs(node.right, remain - node.val)
            path.pop()
        
        dfs(root, targetSum)
        return res