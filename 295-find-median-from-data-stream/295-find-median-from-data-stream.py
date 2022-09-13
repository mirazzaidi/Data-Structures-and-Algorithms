class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.left_max_heap or num < -self.left_max_heap[0]:
            heappush(self.left_max_heap, -num)
        else:
            heappush(self.right_min_heap, num)
        
        if len(self.left_max_heap) - len(self.right_min_heap) > 1:
            heappush(self.right_min_heap, -heappop(self.left_max_heap))
        elif len(self.right_min_heap) - len(self.left_max_heap) > 0:
            heappush(self.left_max_heap, -heappop(self.right_min_heap))
            
            
            

    def findMedian(self) -> float:
        if not self.left_max_heap:
            return 0.0
        if len(self.left_max_heap) - len(self.right_min_heap) > 0:
            return -self.left_max_heap[0]
        else:
            return (-self.left_max_heap[0] + self.right_min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
