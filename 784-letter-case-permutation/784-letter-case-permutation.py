class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def permute(index: int, curr: str):
            if index == len(s):
                res.append(curr)
                return
            
            permute(index+1, curr + s[index])

            if s[index].isalpha():
                permute(index+1, curr + (s[index]).swapcase())
                
        res = []
        permute(0, curr = '')
        return res
            