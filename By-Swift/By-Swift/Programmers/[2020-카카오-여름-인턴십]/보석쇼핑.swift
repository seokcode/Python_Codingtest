import Foundation

func solution(_ gems:[String]) -> [Int] {
    var cart = [String : Int]()
    var ans = [1,gems.count]
    let gemNum = Set(gems).count
    var start = 0
    
    for end in 0..<gems.count {
         cart[gems[end],default: 0] += 1
        
        while (cart.keys.count == gemNum) && (start <= end) {
            
            ans = (ans.last! - ans.first!) > (end-start) ? [start+1, end+1] : ans

            cart[gems[start],default: 0] -= 1
            if cart[gems[start]]! == 0 {
                cart.removeValue(forKey: gems[start])
            }
            start += 1
        }
    }
    return ans
}