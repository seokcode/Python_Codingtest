# Squares of a Sorted Array
> **Easy**
>
> **2021-11-07**
>
> **[Leetcode: 977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)**


## Sol
주어지는 nums 배열 내 숫자를 제곱하고 정렬된 배열로 만드는 문제

## 답안
> Runtime: 216 ms, faster than 95.30% of Swift online submissions for Squares of a Sorted Array.  
> Memory Usage: 15.5 MB, less than 66.44% of Swift online submissions for Squares of a Sorted Array.
```swift
class Solution {
    func sortedSquares(_ nums: [Int]) -> [Int] {
        return nums.map{Int(pow(Double($0),2))}.sorted()
    }
}        
```