class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >=len(grid[0]) or grid[i][j] != '1':
                return
            # mark as visited            
            grid[i][j] = '2'
            
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        
        def bfs(i,j):
            
            q = deque()
            q.append((i,j))
            grid[i][j] = '2'
            
            while q:
                n = len(q)
                for _ in range(n):
                    x,y = q.popleft()

                    for direction in dirs:
                        next_row = x + direction[0]
                        next_col = y + direction[1]
                        if next_row < 0 or next_row >= len(grid) or \
                        next_col < 0 or next_col >=len(grid[0]) or \
                        grid[next_row][next_col] != '1':
                            continue
                        grid[next_row][next_col] = '2'
                        q.append((next_row, next_col))
            
            
        islands = 0
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i,j)
                    islands += 1
        return islands
                    