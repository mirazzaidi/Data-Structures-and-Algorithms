class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:


        def permute(index: int, curr):
            if index == len(s):
                res.append(curr)
                return
            
            permute(index+1, curr + s[index])

            if s[index] not in '0123456789':
                permute(index+1, curr + (s[index]).swapcase())
                
        res = []
        permute(0, curr = '')
        return res
            