class Solution {
    func jump(_ nums: [Int]) -> Int {
        var left = 0
        var right = 0
        var jumpCnt = 0
        
        while right < nums.count-1 {
            jumpCnt += 1
            var furthest = 0
            (left...right).forEach {
                furthest = max(furthest, $0+nums[$0])
            }
            
            left = right+1
            right = furthest
        }
        
        return jumpCnt
    }
}