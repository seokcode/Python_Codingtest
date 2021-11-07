// Runtime: 216 ms, faster than 95.30% of Swift online submissions for Squares of a Sorted Array.
// Memory Usage: 15.5 MB, less than 66.44% of Swift online submissions for Squares of a Sorted Array.
class Solution {
    func sortedSquares(_ nums: [Int]) -> [Int] {
        return nums.map{Int(pow(Double($0),2))}.sorted()
    }
}