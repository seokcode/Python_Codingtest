// Sol 1
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        let s = Array(s)
        var ans = 0
        var start = 0
        var update = [Character: Int]()
        
        for idx in 0..<s.count {
            if update.keys.contains(s[idx]) {
                start = max(update[s[idx]]!, start)
            }
            ans = max(ans, idx-start+1)
            update[s[idx]] = idx+1
        }
        
        return ans
    }
}

// Sol 2
import Foundation

class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var length = 0, chars = [Character]()
        s.forEach({
            if chars.contains($0) {
                chars.removeSubrange(0...chars.firstIndex(of: $0)!)
            }
            chars.append($0)
            length = max(length, chars.count)
        })
        return length
    }
}