import Foundation

func solution(_ enroll:[String], _ referral:[String], _ seller:[String], _ amount:[Int]) -> [Int] {
    var relation = [String: String]()
    var score = [String: Int]()
    
    for i in 0..<enroll.count {
        relation[enroll[i]] = referral[i]
        score[enroll[i]] = 0
    }
    
    for i in 0..<seller.count {
        var cur = seller[i]
        var money = amount[i]*100
        var tax = Int(Double(money)*0.1)
        while cur != "-" {
            if tax >= 1 {
                score[cur]! += money-tax
            } else {
                score[cur]! += money
                break
            }
            
            cur = relation[cur]!
            money = tax
            tax = Int(Double(money)*0.1)
        }
    }
    
    var answer = [Int]()
    for i in enroll {
        answer.append(score[i]!)
    }
    return answer
}