class Solution {
    func generateMatrix(_ n: Int) -> [[Int]] {
        let dx = [0,1,0,-1]
        let dy = [1,0,-1,0]
        
        var result = Array(repeating: Array(repeating: 0, count: n), count: n)
        var cx = 0
        var cy = 0
        var direction = 0
        
        for i in 1...(n*n) {
            result[cx][cy] = i
            let nx = cx + dx[direction]
            let ny = cy + dy[direction]
            
            if (0 <= nx && nx < n) && (0 <= ny && ny < n) && (result[nx][ny] == 0) {
                cx = nx
                cy = ny
            } else {
                direction = (direction+1)%4
                cx += dx[direction]
                cy += dy[direction]
            }
        }
        return result
    }
}