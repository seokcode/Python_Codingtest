# Spiral Matrix
> **Medium**
>
> **2021-08-14**
>
> **[Leetcode: Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)**


## Sol

이런 문제를 만날때마다 풀릴 것 같으면서 이상하게 꼬였는데 너무 어렵게 생각해왔던 것 같다.

먼저 파악해야하는 사항은 이렇다.
1. 방향은 총 4가지이다. 그리고 (오른,아래,왼쪽,위)의 순서가 반복된다(방향의 순서가 정해져있다).
2. 몇번 꺾이는지는 규칙적이지 않다.
3. 하지만 끝에 도달했거나 이미 방문한 곳을 만나면 방향이 전환된다.
4. 마지막 숫자는 가로x세로의 결과이다(ex 4x3 사각형이면 12가 마지막 숫자).


이를 바탕으로 로직을 설계한다.


## 답안
> Runtime: 0 ms, faster than 100.00% of Swift online submissions for Spiral Matrix.  
> Memory Usage: 13.7 MB, less than 95.54% of Swift online submissions for Spiral Matrix.
```swift
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
```

# 또 다른 답안 - 재귀
> Runtime: 0 ms, faster than 100.00% of Swift online submissions for Spiral Matrix.  
> Memory Usage: 13.8 MB, less than 95.54% of Swift online submissions for Spiral Matrix.
```swift
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
```