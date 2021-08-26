# Number of Islands
> **Medium**
>
> **2021-08-26**
>
> **[Leetcode: Number of Islands](https://leetcode.com/problems/number-of-islands)**


## Sol

DFS로 풀이하였다. 방문 기록은 별도의 배열을 만들어 사용하지 않고 grid 배열에 "#" 표시를 하는것으로 사용하였다.


## 답안
```python
class Solution:
    def dfs(self, grid, x, y, R, C):
            dx = [1,0,-1,0]
            dy = [0,1,0,-1]
            
            for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if (0 <= nx < R) and (0 <= ny < C) and (grid[nx][ny] == "1") :
                        grid[nx][ny] = "#"
                        self.dfs(grid, nx, ny, R, C)
                    else: 
                        continue
                    
            return
        
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        answer = 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    grid[i][j] = "#"
                    self.dfs(grid, i, j, R, C)
                    answer += 1
        
        return answer
```