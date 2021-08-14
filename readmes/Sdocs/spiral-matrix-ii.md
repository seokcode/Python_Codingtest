# Spiral Matrix II
> **Medium**
>
> **2021-08-01**
>
> **[Leetcode: Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)**


## Sol
Spiral Matrix I과 다른 점
1. n만 주어진다
2. 무조건 n x n의 정사각형이다
3. 일차원배열을 return하는게 아니라 matrix(사각형 설계도)를 return한다.

먼저 파악해야하는 사항은 I과 똑같다.
1. 방향은 총 4가지이다. 그리고 (오른,아래,왼쪽,위)의 순서가 반복된다(방향의 순서가 정해져있다).
2. 몇번 꺾이는지는 규칙적이지 않다.
3. 하지만 끝에 도달했거나 이미 방문한 곳을 만나면 방향이 전환된다(여기서는 굳이 방문 말고 값이 있으면 전환으로 구현하였음).
4. 마지막 숫자는 n*n이다.

이를 바탕으로 로직을 설계한다.

## 답안
> Runtime: 8 ms, faster than 15.00% of Swift online submissions for Spiral Matrix II.  
> Memory Usage: 14 MB, less than 72.50% of Swift online submissions for Spiral Matrix II.
```swift
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
```