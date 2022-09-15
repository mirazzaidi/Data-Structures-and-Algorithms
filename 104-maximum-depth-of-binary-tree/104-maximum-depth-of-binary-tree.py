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
                return 0
            
            left = get_max_depth(root.left, curr_depth+1)
            right = get_max_depth(root.right, curr_depth+1)
            return 1 + max(left, right)
        return get_max_depth(root)
        # return ÷max_dep[0]