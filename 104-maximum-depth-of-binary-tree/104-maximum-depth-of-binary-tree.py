# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def get_max_depth(root, curr_depth=1):
            if not root:
                return
            
            if not root.left and not root.right:
                max_dep[0] = max(curr_depth, max_dep[0])
            
            get_max_depth(root.left, curr_depth+1)
            get_max_depth(root.right, curr_depth+1)
        
        if not root:
            return 0
        max_dep = [0]
        get_max_depth(root)
        return max_dep[0]