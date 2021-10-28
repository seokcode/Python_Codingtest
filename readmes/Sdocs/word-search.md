# Word Search
> **Medium**
>
> **2021-10-28**
>
> **[Leetcode: Word Search](https://leetcode.com/problems/word-search)**


## Sol

단어의 시작 문자와 일치하는 곳을 찾고 그 위치부터 dfs를 통해 탐색해나갔다.  

## 답안
> Runtime: 216 ms, faster than 87.27% of Swift online submissions for Word Search.  
> Memory Usage: 14.3 MB, less than 45.76% of Swift online submissions for Word Search.
```swift
class Solution {
    func exist(_ board: [[Character]], _ word: String) -> Bool {
        let R = board.count
        let C = board[0].count
        var visit = Array(repeating: Array(repeating: false, count: C), count: R)
        let word_lst = Array(word)
        
        for i in 0..<R {
            for j in 0..<C {
                if board[i][j] == word_lst[0] {
                    visit[i][j] = true
                    if findWord(board, &visit, word_lst, 1, (i,j)) {
                        return true
                    }
                    visit[i][j] = false
                }
            }
        }
        return false
    }
    
    func findWord(_ board: [[Character]], _ visit: inout [[Bool]], _ word: [Character], _ idx: Int, _ loc: (Int, Int)) -> Bool {
        let R = board.count
        let C = board[0].count
        let dx = [0,1,0,-1]
        let dy = [1,0,-1,0]
        
        if idx == word.count {
            return true
        }
        
        for d in 0..<4 {
            let nx = loc.0 + dx[d]
            let ny = loc.1 + dy[d]
            if (nx >= 0 && nx < R) && (ny >= 0 && ny < C) && !visit[nx][ny] {
                if board[nx][ny] == word[idx] {
                    visit[nx][ny] = true
                    if findWord(board, &visit, word, idx+1, (nx,ny)) {
                        return true
                    }
                    visit[nx][ny] = false
                }
            }
        }
        return false
    }
}
```