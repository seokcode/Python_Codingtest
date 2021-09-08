import Foundation

func solution(_ number:String, _ k:Int) -> String {
    let numbers = Array(number).map{Int(String($0))!}
    var delete = k
    var answer = [Int]()
    
    for (idx,n) in numbers.enumerated() {
        while (answer.count > 0 && answer.last! < n && delete > 0) {
            answer.popLast()
            delete -= 1
        }
        
        answer.append(n)
    }
    
    if delete > 0 { for _ in (0..<delete) { answer.popLast() } }
    return answer.map{String($0)}.joined()
}