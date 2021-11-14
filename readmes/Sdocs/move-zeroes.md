# Move Zeroes
> **Easy**
>
> **2021-11-14**
>
> **[Leetcode: Move Zeroes](https://leetcode.com/problems/move-zeroes)**


## Sol

배열 내의 0을 찾아서 제거하고 배열 뒤에 붙이는 문제.  
filter를 사용하여 0을 없앤 배열을 만들고 원본 배열과의 길이 차이만큼 0을 붙여주었다.

## 답안
> Runtime: 176 ms, faster than 54.06% of Swift online submissions for Move Zeroes.  
> Memory Usage: 15.3 MB, less than 9.97% of Swift online submissions for Move Zeroes.
```swift
class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        let noneZeroArr = nums.filter { $0 != 0 }
        nums = noneZeroArr + Array(repeating: 0, count: (nums.count - noneZeroArr.count))
    }
}
```