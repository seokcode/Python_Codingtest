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