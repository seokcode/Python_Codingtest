import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var boards = board
    var storage: [Int] = []
    var answer = 0
    
    for m in moves {
        var row = 0
        while row < board.count {
            if boards[row][m-1] != 0 {
                if storage.last == boards[row][m-1] {                    
                    storage.removeLast()
                    answer += 2
                }else {
                    storage.append(boards[row][m-1])   
                }
                boards[row][m-1] = 0
                break
            }
            row += 1
        }
    }
    return answer
}