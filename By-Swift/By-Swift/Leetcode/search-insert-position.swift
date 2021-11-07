// Runtime: 28 ms, faster than 90.92% of Swift online submissions for Search Insert Position.
// Memory Usage: 14.4 MB, less than 24.44% of Swift online submissions for Search Insert Position.
class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        var left = 0
        var right = nums.count-1
        
        while left <= right {
            let mid = left + ((right-left)/2)
            if nums[mid] == target {
                return mid
            }
            
            if target > nums[mid] {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        
        return left
    }
}