import Foundation

struct Boxer {
    let idx: Int
    let rate: Double
    let winHeavy: Int
    let weight: Int
}

func solution(_ weights:[Int], _ head2head:[String]) -> [Int] {
    var record = [Boxer]()
    
    for (mIdx,i) in head2head.enumerated() {
        var game = 0
        var win = 0
        var heavy = 0
        
        for (eIdx,j) in Array(i).enumerated() {
            switch j {
            case "L":
                game += 1
            case "W":
                game += 1
                win += 1
                if weights[eIdx] > weights[mIdx] {
                    heavy += 1
                }
            default:
                break
            }
        }
        let rate = game > 0 ? Double(win)/Double(game) : 0.0
        record.append(Boxer(idx: mIdx+1, rate: rate, winHeavy: heavy, weight: weights[mIdx]))
    }
    
    let answer = record.sorted{
        if $0.rate > $1.rate {
            return true
        } else if $0.rate == $1.rate {
            if $0.winHeavy > $1.winHeavy {
                return true
            } else if $0.winHeavy == $1.winHeavy {
                if $0.weight > $1.weight {
                    return true
                } else if $0.weight == $1.weight {
                    return $0.idx < $1.idx
                }
            }
        }
        return false
    }.map{Int($0.idx)}
    
    return answer
}