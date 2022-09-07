# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root) -> int:   
        
            if not root:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            
            return 1 + max(left_depth, right_depth)
        
        return depth(root)