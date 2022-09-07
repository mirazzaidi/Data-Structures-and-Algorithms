# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # def height(root) -> int:
        #     if not root: return 0
        #     return 1 + max(height(root.left), height(root.right))
        def rec(root):
            
            if not root:
                return True, 0
            is_left_bal, left_h = rec(root.left)
            is_right_bal, right_h = rec(root.right)
            
            if is_left_bal and is_right_bal and abs(left_h-right_h) <= 1:
                return True, 1 + max(left_h,right_h)
            else:
                return False, 1 + max(left_h,right_h)
        return rec(root)[0]