# Two Sum II - Input Array Is Sorted
> **Easy**
>
> **2021-11-14**
>
> **[Leetcode: Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)**


## Sol

오름차순으로 정렬된 배열이 주어지고 배열 내 원소 두개를 합쳐서 target이 되는 원소들의 인덱스를 return하는 문제. 투 포인터를 사용하여 풀이해주었다.

## 답안
> Runtime: 28 ms, faster than 89.98% of Swift online submissions for Two Sum II - Input Array Is Sorted.  
> Memory Usage: 14.5 MB, less than 19.30% of Swift online submissions for Two Sum II - Input Array Is Sorted.
```swift
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
```