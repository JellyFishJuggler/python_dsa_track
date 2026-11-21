# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0
        
        l = self.height(root.left)
        r = self.height(root.right)

        self.diameter = max(self.diameter, l+r)

        return 1 + max(l,r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter: int = 0
        self.height(root)
        return self.diameter