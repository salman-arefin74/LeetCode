# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while len(queue):
            level = []
            for i in range(len(queue)):
                tempNode = queue.popleft()
                level.append(tempNode.val)
                if tempNode.left:
                    queue.append(tempNode.left)
                if tempNode.right:
                    queue.append(tempNode.right)
            result.append(level)

        return result

        