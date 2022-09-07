class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:     
            
        def is_unit_valid(units)->bool:
            unique = set()
            for unit in units:
                if unit == '.':
                    continue
                if unit in unique:
                    return False
                unique.add(unit)
            return True
        
        for row in board:
            if not is_unit_valid(row):
                return False
        
        for col in zip(*board):
            if not is_unit_valid(col):
                return False
        
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not is_unit_valid(square):
                    return False
        return True