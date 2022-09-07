class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        ransom_note_counter = Counter(ransom_note)
        magazine_counter = Counter(magazine)
        
        for char, count in ransom_note_counter.items():
            if char not in magazine_counter or count > magazine_counter[char]:
                return False
        return True
        