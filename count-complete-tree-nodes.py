# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.preOrderTraversal(root)
        return self.count
    def preOrderTraversal(self, root: Optional[TreeNode]) -> None:
        if root:
            self.count += 1
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)
