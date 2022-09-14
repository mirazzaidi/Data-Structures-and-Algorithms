class Solution:
    
    def dfs(self, grid: List[List[str]], i, j):
        q = deque()
        
        q.append((i,j))
        grid[i][j] = True
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q:
            r, c = q.pop()            
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]
                
                if 0 <= nr < len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=='1':
                    grid[nr][nc] = True
                    q.append((nr, nc))
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    islands += 1
        return islands
                    
        
        
        