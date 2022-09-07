class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = [0]*26
        for char in s:
            index = ord(char) - ord('a')
            char_count[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            char_count[index] -= 1
        for count in char_count:
            if count != 0:
                return False
        
        return True