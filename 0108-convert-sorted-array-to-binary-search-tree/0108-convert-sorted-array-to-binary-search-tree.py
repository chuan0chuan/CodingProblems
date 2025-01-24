# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # step 1 : define the para and return value of recursive function:
    def travesal(self, nums: List[int], left, right):
        # step 2: find the ending break condition of the function:
        if left > right:
            return None
        # step 3: know the each level travesal:
        mid = ( left + right ) // 2
        root = TreeNode(nums[mid])
        root.left = self.travesal(nums, left, mid -1)
        root.right = self.travesal(nums, mid + 1, right)
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.travesal(nums, 0 , len(nums) - 1)
        return root

        