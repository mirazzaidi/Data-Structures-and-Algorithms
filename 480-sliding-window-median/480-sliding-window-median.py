
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        def rebalance_heaps():
            if len(max_heap) - len(min_heap) > 1:
                heappush(min_heap, -heappop(max_heap))
            elif len(max_heap) < len(min_heap):
                heappush(max_heap, -heappop(min_heap))
        
        def remove_from_heap(item, heap):
            index = heap.index(item)
            heap[index]= heap[-1]
        
            del heap[-1]
            heapify(heap)
            rebalance_heaps()
            
        
        min_heap = []
        max_heap = []
        ans = []
        
        start, end = 0, 0
        for end in range(len(nums)):
            num = nums[end]
            
            if not max_heap or num < -max_heap[0]:
                heappush(max_heap, -num)
            else:
                heappush(min_heap, num)
            
            rebalance_heaps()

            
            if end - start+1 >= k:
                            
                if len(max_heap) > len(min_heap):
                    ans.append(-max_heap[0]/1.0)
                elif len(max_heap) == len(min_heap):
                    ans.append((-max_heap[0] + min_heap[0])/2.0)
                
                item_to_remove = nums[start]
                start += 1
                if item_to_remove <= -max_heap[0]:
                    remove_from_heap(-item_to_remove, max_heap)
                else:
                    remove_from_heap(item_to_remove, min_heap)
        return ans
                
        
        