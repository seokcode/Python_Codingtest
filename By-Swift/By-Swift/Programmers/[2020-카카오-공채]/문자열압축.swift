import Foundation

func solution(_ s:String) -> Int {
    var answer = Int.max
    
    if s.count <= 1 { return 1 }
    
    for i in 1...(s.count/2) {
        var repeatation = 1
        var remain = 0
        var last = ""
        
        for j in stride(from: 0, to: s.count, by: i) {
            let range = s.index(s.startIndex, offsetBy: j)..<s.index(s.startIndex, offsetBy: min(j+i,s.count))
            let current = String(s[range])
            
            if last == current {
                repeatation += 1
            } else {
                remain += (current.count+(repeatation >= 2 ? (repeatation >= 10 ? 2 : 1) : 0))
                repeatation = 1
                last = current
            }
        }
        
        answer = min(answer, remain+(repeatation >= 2 ? (repeatation >= 10 ? 2 : 1) : 0))
    }
    
    return answer
}