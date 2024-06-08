#Medium
#Array / String
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Helper function to check if a list has duplicates (excluding '.')
        def is_valid_unit(unit: List[str]) -> bool:
            seen = set()
            for num in unit:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
            return True
        
        # Check rows
        for row in board:
            if not is_valid_unit(row):
                return False
        
        # Check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not is_valid_unit(column):
                return False
        
        # Check 3x3 subgrids
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                subgrid = [
                    board[row + i][col + j]
                    for i in range(3)
                    for j in range(3)
                ]
                if not is_valid_unit(subgrid):
                    return False
        
        return True