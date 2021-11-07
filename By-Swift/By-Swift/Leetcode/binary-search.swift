// Runtime: 280 ms, faster than 98.55% of Swift online submissions for Binary Search.
// Memory Usage: 14.1 MB, less than 63.80% of Swift online submissions for Binary Search.
class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var left = 0
        var right = nums.count-1
        
        while left <= right {
            let mid = left + (right - left) / 2
            
            if nums[mid] == target {
                return mid
            }
            
            if target > nums[mid] {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        
        return -1
    }
}