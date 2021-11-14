class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        let noneZeroArr = nums.filter { $0 != 0 }
        nums = noneZeroArr + Array(repeating: 0, count: (nums.count - noneZeroArr.count))
    }
}