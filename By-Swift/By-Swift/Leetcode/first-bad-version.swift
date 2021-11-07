/**
 * The knows API is defined in the parent class VersionControl.
 *     func isBadVersion(_ version: Int) -> Bool{}
 */

// Runtime: 4 ms, faster than 69.03% of Swift online submissions for First Bad Version.
// Memory Usage: 13.6 MB, less than 94.36% of Swift online submissions for First Bad Version.
class Solution : VersionControl {
    func firstBadVersion(_ n: Int) -> Int {
        var left = 1
        var right = n
        
        while left <= right {
            let mid = left + ((right-left)/2)
            if isBadVersion(mid) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        
        return left
    }
}