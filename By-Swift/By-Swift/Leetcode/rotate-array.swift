class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        var k = k % nums.count 
        let n = nums.count - 1
        reverse(&nums, 0, n)
        reverse(&nums, 0, k - 1)
        reverse(&nums, k, n)
    }
    
    func reverse(_ nums: inout [Int], _ s: Int, _ e: Int) {
        var s = s 
        var e = e 
        while s < e {
            nums.swapAt(s, e)
            s += 1
            e -= 1
        }
    }
}