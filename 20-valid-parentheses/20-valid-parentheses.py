class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        
        for ch in s:
            
            if ch in '([{':
                stack.append(ch)
            
            else: # closing bracket found
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top+ch not in ['()', '{}', '[]']:
                    return False
        return len(stack) == 0
                    