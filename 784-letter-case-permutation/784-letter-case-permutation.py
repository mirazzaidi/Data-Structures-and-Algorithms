class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def flip(char):
            if char.isupper():
                return char.lower()
            else:
                return char.upper()
            
        def permute(index: int, curr):
            if index == len(s):
                res.append(curr)
                return
            
            permute(index+1, curr + s[index])

            if s[index] not in '0123456789':
                permute(index+1, curr + flip(s[index]))
                
        res = []
        permute(0, curr = '')
        return res
            