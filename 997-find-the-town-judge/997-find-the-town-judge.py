class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adjlist = {}
        indegree = {}
        outdegree = {}
        for i in range(1,n+1):
            adjlist[i] = []
            indegree[i] = 0
            outdegree[i] = 0
        
        for trust_item in trust:
            truster, trustee = trust_item[0], trust_item[1]
            adjlist[trustee].append(truster)
            outdegree[truster] += 1
            indegree[trustee] += 1
        
        for i in range(1,n+1):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1
        
        