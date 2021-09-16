import Foundation

func grade(_ score: Float) -> String {
    switch score {
        case (90...):
            return "A"
        case (80..<90):
            return "B"
        case (70..<80):
            return "C"
        case (50..<70):
            return "D"
        default:
            return "F"
    }
}

func rotate(_ subject: [[Int]]) -> [[Int]] {
    let N = subject.count
    let M = subject.first!.count
    var result = Array(repeating: Array(repeating: 0, count: N), count: M)
    
    for i in 0..<N {
        for j in 0..<M {
            result[j][i] = subject[i][j]
        }
    }
    
    return result
}

func solution(_ scores:[[Int]]) -> String {
    var answer = ""
    let tScore = rotate(scores)
    
    for (idx,item) in tScore.enumerated() {
        var len = item.count
        var sum = item.reduce(0, {$0+$1})
        if (item.max() == item[idx] || item.min() == item[idx]) && item.filter({ $0 == item[idx] }).count == 1
        {
            sum -= item[idx]
            len -= 1
        }
        answer += grade(Float(sum/len))
    }
    
    return answer
}