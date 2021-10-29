class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        var pointer = (0,0)
        var furthest = 0
        let destination = nums.count-1
        
        while pointer.1 < destination {
            if pointer.0 > pointer.1 {
                return false
            }
            
            for i in pointer.0...pointer.1 {
                furthest = max(furthest, i+nums[i])
            }
            
            pointer = (pointer.1+1, furthest)
        }
        return true
    }
}   