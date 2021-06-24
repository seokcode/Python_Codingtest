// 브루트포스
import Foundation

func solution(_ citations:[Int]) -> Int {
    var cit = citations.sorted()
    var h = 0
    var answer = 0
    
    while true {    
        let citated = cit.filter{$0 >= h}.count
        
        if citated >= h {
            answer = h
            h += 1
        } else {
            return answer
            break
        }
    }
}

// 이분탐색
import Foundation

func solution(_ citations:[Int]) -> Int {
    var low = 0
    var high = citations.max()!
    
    while low <= high {
        let mid = (low+high)/2
        let citated = citations.filter{$0 >= mid}.count
        
        if citated < mid {
            high = mid-1
        } else {
            low = mid+1
        }
    }
    
    return high
}