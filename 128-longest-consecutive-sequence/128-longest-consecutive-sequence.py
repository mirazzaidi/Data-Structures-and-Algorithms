class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if num-1 in num_set:
                continue
            curr_len = 1
            while num + 1 in num_set:
                curr_len += 1
                num += 1
            max_len = max(curr_len, max_len)
        return max_len