# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None   # 用来保存中序遍历上一个节点的值

        def inorder(node):
            if not node:
                return True
            # 先判断左子树
            if not inorder(node.left):
                return False
            # 当前节点必须大于前一个节点
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val
            # 再判断右子树
            return inorder(node.right)

        return inorder(root)
            