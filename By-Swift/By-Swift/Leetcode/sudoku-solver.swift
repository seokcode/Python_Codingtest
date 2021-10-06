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