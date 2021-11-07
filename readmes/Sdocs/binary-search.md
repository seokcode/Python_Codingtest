# Binary Search
> **Easy**
>
> **2021-11-07**
>
> **[Leetcode: 704. Binary Search](https://leetcode.com/problems/binary-search/)**


## Sol
주어진 nums 배열에 target이 있다면 그 인덱스를 return하는 문제. 없다면 -1를 return한다.
문제 이름처럼 이진탐색을 통해 풀이해주었다.

## 답안
> Runtime: 280 ms, faster than 98.55% of Swift online submissions for Binary Search.
> Memory Usage: 14.1 MB, less than 63.80% of Swift online submissions for Binary Search.
```swift
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
```