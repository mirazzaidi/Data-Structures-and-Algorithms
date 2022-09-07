class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i, num in enumerate(nums):
            if i < k:
                heappush(min_heap, num)
            elif min_heap[0] < num:
                heappushpop(min_heap, num)
        return min_heap[0]
                