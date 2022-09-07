# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root) -> int:
            if not root: return 0
            return 1 + max(height(root.left), height(root.right))
        
        if not root:
            return True
    
        if self.isBalanced(root.left) and self.isBalanced(root.right):    
            left_height = height(root.left)
            right_height = height(root.right)

            if abs(left_height - right_height) <= 1:
                return True
        return False