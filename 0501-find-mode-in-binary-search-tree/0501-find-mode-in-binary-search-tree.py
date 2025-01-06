# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _init_(self):
        self.counts = {}

    def firstPass(self, cur):
        if cur is None:
            return
        self.firstPass(cur.left)
        self.counts[cur.val] = self.counts.get(cur.val, 0) + 1
        self.firstPass(cur.right)
    
    def secondPass(self, cur, maxFreq, result):
        if cur is None:
            return
        self.secondPass(cur.left, maxFreq, result)
        if self.counts[cur.val] == maxFreq:
            result.add(cur.val)
        self.secondPass(cur.right, maxFreq, result)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.counts = {}
        self.firstPass(root)
        maxFreq = max(self.counts.values(), default = 0)

        result = set()
        self.secondPass(root, maxFreq,result)
        return list(result)