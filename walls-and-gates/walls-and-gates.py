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
        def add_room(row, col, distance):
            if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]) and rooms[row][col] == self.INF:
                rooms[row][col] = distance
                q.append((row, col))
        
        q = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i,j))
        while q:
            count = len(q)
            for _ in range(count):
                row, col = q.popleft()
                distance = rooms[row][col] + 1
                add_room(row-1, col, distance)
                add_room(row, col-1, distance)
                add_room(row+1, col, distance)
                add_room(row, col+1, distance)
