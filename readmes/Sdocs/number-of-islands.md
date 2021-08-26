# Number of Islands
> **Medium**
>
> **2021-08-26**
>
> **[Leetcode: Number of Islands](https://leetcode.com/problems/number-of-islands)**


## Sol

DFS로 풀이하였다.


## 답안
```swift
class Solution {
    func dfs(_ grid: [[Character]], _ visited: inout [[Bool]], _ x: Int, _ y: Int) {
        let R = grid.count
        let C = grid.first!.count
        let dx = [1,0,-1,0]
        let dy = [0,1,0,-1]
        
        for d in 0..<4 {
            let nx = x + dx[d]
            let ny = y + dy[d]
            
            if (0 <= nx && nx < R) && (0 <= ny && ny < C) && (grid[nx][ny] == "1") && !visited[nx][ny] {
                visited[nx][ny] = true
                dfs(grid, &visited, nx, ny)
            }
        }
        
        return
    }
    
    func numIslands(_ grid: [[Character]]) -> Int {
        var visited = Array(repeating: Array(repeating: false, count: grid.first!.count), count: grid.count)
        var answer = 0
        
        for i in 0..<grid.count {
            for j in 0..<grid.first!.count {
                if grid[i][j] == "1" && !visited[i][j] {
                    visited[i][j] = true
                    dfs(grid, &visited, i, j)
                    answer += 1
                }
            }
        }
        
        return answer
    }
}
```