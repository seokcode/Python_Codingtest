# Sudoku Solver
> **Hard**
>
> **2021-09-24**
>
> **[Leetcode: Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)**


## Sol
완탐, 백트래킹에 약한 것 같아서 선택한 문제.  

스도쿠를 한번 순회하여 빈 칸을 배열에 담아두고 빈칸에 1~9까지 모든 수를 넣어보면서 가능한 숫자로 가득 채워진 경우 True를 return한다.    
옳지 않은 숫자가 들어가서 완성되지 못하는 경우에는 board[r][c] = "."로 다시 초기화해준다 **(매우 중요)**

## 답안
> Runtime: 436 ms, faster than 36.37% of Python3 online submissions for Sudoku Solver.  
> Memory Usage: 14.5 MB, less than 29.34% of Python3 online submissions for Sudoku Solver.
```python
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
```