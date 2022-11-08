# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal = []
        self.inorder(root)
        return self.traversal

    def inorder(self, root: Optional[TreeNode]) -> None:
        if root:
            self.inorder(root.left)
            self.traversal.append(root.val)
            self.inorder(root.right)

