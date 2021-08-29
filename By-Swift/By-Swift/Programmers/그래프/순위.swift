import Foundation

func solution(_ n:Int, _ results:[[Int]]) -> Int {
    var board = Array(repeating: Array(repeating: "?", count: n), count: n)
    
    for r in results {
        board[r.first!-1][r.last!-1] = "WIN"
        board[r.last!-1][r.first!-1] = "LOSE"
    }
    
    for k in 0..<n {
        for i in 0..<n {
            for j in 0..<n {
                if board[i][j] == "?" {
                    if board[i][k] == "WIN" && board[k][j] == "WIN" {
                        board[i][j] = "WIN"
                        board[j][i] = "LOSE"
                    } else if board[i][k] == "LOSE" && board[k][j] == "LOSE" {
                        board[i][j] = "LOSE"
                        board[j][i] = "WIN"
                    }
                }
            }
        }
    }
    
    var answer = 0
    board.forEach {
        if $0.filter { $0 == "?" }.count == 1 {
            answer += 1
        }
    }
    
    return answer
}