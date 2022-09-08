from typing import (
    List,
)
from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    INF = 2147483647
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        q = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        while q:
            count = len(q)
            for _ in range(count):
                row, col = q.popleft()
                distance = rooms[row][col]
                
                for direction in directions:
                    next_row = row + direction[0]
                    next_col = col + direction[1]

                    if (0 <= next_row < len(rooms)) and (0 <= next_col < len(rooms[0])):
                        if rooms[next_row][next_col] == self.INF:

                            rooms[next_row][next_col] = rooms[row][col] + 1
                            q.append((next_row, next_col))
            

