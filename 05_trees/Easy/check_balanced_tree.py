# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self, root: TreeNode | None):
        if not root:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: TreeNode | None) -> bool:
        
        if not root:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        return False