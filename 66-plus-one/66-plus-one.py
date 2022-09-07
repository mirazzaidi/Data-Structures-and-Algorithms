class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        [9]
        [9]
        [0,1]
        """
        digits.reverse()
        carry = 1
        for i in range(len(digits)):
            digits[i] += carry
            carry = digits[i]//10
            digits[i] = digits[i]%10
            
        if carry == 1:
            digits.append(carry)
        digits.reverse()
        return digits