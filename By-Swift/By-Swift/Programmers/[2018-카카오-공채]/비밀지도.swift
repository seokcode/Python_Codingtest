import Foundation

func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    var answer: [String] = []

    zip(arr1, arr2).forEach {
        let merge = String($0.0|$0.1, radix:2)
        let frame = Array(String(repeating: "0", count: n - merge.count) + merge)
        answer.append(frame.map{ $0 == "1" ? "#" : " " }.joined())
    }
    return answer
}