# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal = []
        self.preorder(root)
        return self.traversal

    def preorder(self, root: Optional[TreeNode]) -> None:
        if root:
            self.traversal.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

