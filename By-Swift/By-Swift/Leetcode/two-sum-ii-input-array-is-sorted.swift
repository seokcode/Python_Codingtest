class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        var left = 0
        var right = numbers.count - 1
        
        while left < right {
            let sum = numbers[left] + numbers[right]
            
            if sum == target {
                break
            } else if sum > target {
                right -= 1
            } else {
                left += 1
            }
        }
        
        return [left+1, right+1]
    }
}