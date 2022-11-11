# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compareSides(root.left, root.right)

    def compareSides(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        elif left and right and left.val == right.val:
            return self.compareSides(left.left, right.right) and self.compareSides(left.right, right.left)
        else:
            return False