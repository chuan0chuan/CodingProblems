# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _init_(self):
        self.parent = None

    def traversal(self, cur, val):
        if cur is None:
            node = TreeNode(val)
            if val > self.parent.val:
                self.parent.right = node
            else:
                self.parent.left = node
            return
        
        #if not leave, traversal
        self.parent = cur
        if cur.val > val:
            self.traversal(cur.left, val)
        if cur.val < val:
            self.traversal(cur.right, val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #self.parent = TreeNode(0)
        if root is None:
            return TreeNode(val)
        self.traversal(root, val)
        return root
        