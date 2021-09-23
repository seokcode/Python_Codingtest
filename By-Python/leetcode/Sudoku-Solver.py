class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        blank = []
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    blank.append([i,j])            
        
        self.makeSudoku(0, board, blank)
        
    def makeSudoku(self, k, board, blank):
        if k == len(blank): 
            return True
        
        r, c = blank[k]
        for i in map(str, range(1,10)):
            if self.uniqueValue(board, r, c, i):
                board[r][c] = i
                if self.makeSudoku(k+1, board, blank): 
                    return True
        
        board[r][c] = "."
        return False
    
    def uniqueValue(self, board, r, c, val) -> bool:
        for i in range(9):
            if board[r][i] == val or board[i][c] == val:
                return False
        
        boxRow, boxCol = (r//3)*3, (c//3)*3
        for i in range(3):
            for j in range(3):
                if board[boxRow+i][boxCol+j] == val:
                    return False
        return True