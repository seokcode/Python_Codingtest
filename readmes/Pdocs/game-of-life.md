# Game of Life
> **Medium**
>
> **2021-10-10**
>
> **[Leetcode: Game of Life](https://leetcode.com/problems/game-of-life)**


## Sol
```markdown
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

* Any live cell with fewer than two live neighbors dies as if caused by under-population.
* Any live cell with two or three live neighbors lives on to the next generation.
* Any live cell with more than three live neighbors dies, as if by over-population.
* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
```
## 답안
> Runtime: 28 ms, faster than 94.70% of Python3 online submissions for Game of Life.  
> Memory Usage: 14.4 MB, less than 12.20% of Python3 online submissions for Game of Life.
```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:    
        N, M = len(board), len(board[0])
        nxtGen = [[False] * M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                live, dead = self.checkAroundMe(board,i,j)
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        nxtGen[i][j] = True
                elif board[i][j] == 0:
                    if live == 3:
                        nxtGen[i][j] = True
            
        for i in range(N):
            for j in range(M):
                if nxtGen[i][j]:
                    board[i][j] ^= 1
        
    def checkAroundMe(self, board, r, c):
        N, M = len(board), len(board[0])
        dx = [0,-1,-1,-1,0,1,1,1]
        dy = [-1,-1,0,1,1,1,0,-1]
        
        cntLive, cntDead = 0,0
        for d in range(8):
            nr, nc = r+dx[d], c+dy[d]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 1:
                    cntLive += 1
                else:
                    cntDead += 1
        
        return cntLive, cntDead
```