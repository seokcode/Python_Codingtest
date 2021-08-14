// 답안 1
class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        if matrix.isEmpty { return [] }
        
        let dx = [0,1,0,-1]
        let dy = [1,0,-1,0]
        
        let row = matrix.count
        let col = matrix.first!.count
        var visited = Array(repeating: Array(repeating: false, count: col), count: row)
        var cx = 0
        var cy = 0
        var direction = 0
        var result: [Int] = []
        
        for i in 0..<(row*col) {
            result.append(matrix[cx][cy])
            visited[cx][cy] = true
            let nx = cx + dx[direction]
            let ny = cy + dy[direction]
            
            if (0 <= nx && nx < row) && (0 <= ny && ny < col) && !visited[nx][ny] {
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

// 답안 2 - 재귀
class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        var res = [Int](), matrix = matrix
        helper(&matrix, &res, 0, 0, 0)
        return res
    }

    func helper(_ matrix: inout [[Int]], _ res: inout [Int], _ x: Int, _ y: Int, _ direc: Int) {
        if x < 0 || x >= matrix.count || y < 0 || y >= matrix[x].count || matrix[x][y] == -987654 { return }
        res += [ matrix[x][y] ]
        matrix[x][y] = -987654
        if direc == 0 {
            helper(&matrix, &res, x, y+1, 0) // right
            helper(&matrix, &res, x+1, y, 0) // down
            helper(&matrix, &res, x, y-1, 0) // left
            helper(&matrix, &res, x-1, y, 1) // up
        }
        if direc == 1 {
            helper(&matrix, &res, x-1, y, 1) // up
            helper(&matrix, &res, x, y+1, 0) // right
        }
    }
}