class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right = 0, 0
        unique_chars = {}
        max_len = 0
        
        while right < len(s):
            if s[right] in unique_chars:
                left = max(left, unique_chars[s[right]] + 1)

            unique_chars[s[right]] = right
            curr_len = right - left + 1
            max_len = max(curr_len, max_len)
            right += 1
        return max_len
                
                
                
            
        