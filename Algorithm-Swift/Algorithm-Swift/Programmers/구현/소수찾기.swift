import Foundation

func combinations(_ array: [String]) -> Set<String> {
    if array.count == 0 { return [] }

    let answerArray = (0..<array.count).flatMap { i -> [String] in
        var removedArray = array
        let elem = removedArray.remove(at: i)
        return [elem] + combinations(removedArray).map { elem + $0 }
    }

    return Set(answerArray)
}

func sosu(_ num: Int) -> Bool {
    var check = 2
    if num < 2 { return false }
    
    while (check*check) <= num {
        if num % check == 0 { return false }
        check += 1
    }
    return true
}

func solution(_ numbers:String) -> Int {
    let arrs = combinations(numbers.map{String($0)})
    var answer: [Int] = []    
    
    for ar in arrs {
        if sosu(Int(ar)!) && !answer.contains(Int(ar)!) {
            answer.append(Int(ar)!)
        }
    }
    return answer.count
}