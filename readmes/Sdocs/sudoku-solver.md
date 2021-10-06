# Sudoku Solver
> **Hard**
>
> **2021-10-06**
>
> **[Leetcode: Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)**


## Sol
완탐, 백트래킹에 약한 것 같아서 선택한 문제. 파이썬으로 한번 풀었던 문제이지만 2주정도 지나고 다시 풀었는데 1트에 통과 크크

스도쿠를 한번 순회하여 빈 칸을 배열에 담아두고 빈칸에 1~9까지 모든 수를 넣어보면서 가능한 숫자로 가득 채워진 경우 True를 return한다.    
옳지 않은 숫자가 들어가서 완성되지 못하는 경우에는 board[r][c] = "."로 다시 초기화해준다 **(매우 중요)**

## 답안
> Runtime: 44 ms, faster than 88.07% of Swift online submissions for Sudoku Solver.  
> Memory Usage: 14.3 MB, less than 80.73% of Swift online submissions for Sudoku Solver.
```swift
class Solution {
    func solveSudoku(_ board: inout [[Character]]) {
        var stack = [(Int,Int)]()
        
        for i in 0..<9 {
            for j in 0..<9 {
                if board[i][j] == "." {
                    stack.append((i,j))
                }
            }
        }
        
        sudoku(&board, stack, 0)
    }
    
    func sudoku(_ board: inout [[Character]], _ stack: [(Int,Int)], _ idx: Int) -> Bool {
        if idx > stack.count-1 {
            return true
        }
        
        let pos = stack[idx]
        
        for i in 1...9 {
            if checkValid(board, pos.0, pos.1, Character(String(i))) {
                board[pos.0][pos.1] = Character(String(i))
                if sudoku(&board, stack, idx+1) {
                    return true
                }
                board[pos.0][pos.1] = "."
            }
        }
        
        return false
    }
    
    func checkValid(_ board: [[Character]], _ r: Int, _ c: Int, _ num: Character) -> Bool {
        for i in 0..<9 {
            if board[r][i] == num || board[i][c] == num {
                return false
            }
        }
        
        let x = Int(r/3) * 3
        let y = Int(c/3) * 3
        
        for i in 0..<3 {
            for j in 0..<3 {
                if board[x+i][y+j] == num {
                    return false
                }
            }
        }
        
        return true
    }
}
```