# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nlist = nestedList
        self.index = 0
        self.stack = deque()
        self.flat_list = deque()
        for item in nestedList:
            if item.isInteger():
                self.flat_list.append(item.getInteger())
            else:        
                self.stack.append(item)
                self.flatten()

        
    
    def flatten(self):
        item = self.stack.pop()
        
        if item.isInteger():
            self.flat_list.append(item.getInteger())
        else:
            for it in item.getList():
                self.stack.append(it)
                self.flatten()
                
                
        
    
    def next(self) -> int:
        return self.flat_list.popleft()
        
        
                          
    
    def hasNext(self) -> bool:
        return len(self.flat_list) > 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())