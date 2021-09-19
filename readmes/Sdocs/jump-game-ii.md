# Jump Game II
> **Medium**
>
> **2021-09-19**
>
> **[Leetcode: 45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)**


## Sol 
`left`는 갈 수 있는 최소 지점, `right`는 갈 수 있는 최대 지점이다. 만약 갈 수 있는 최대 지점이 lastIndex 이상이면 종료된다.


## Two Pointer 풀이

> Runtime: 108 ms, faster than 59.83% of Swift online submissions for Jump Game II.  
> Memory Usage: 14.4 MB, less than 39.32% of Swift online submissions for Jump Game II.
```swift
class Solution {
    func jump(_ nums: [Int]) -> Int {
        var left = 0 // `left`는 갈 수 있는 최소 지점
        var right = 0 // `right`는 갈 수 있는 최대 지점
        var jumpCnt = 0
        
        while right < nums.count-1 {
            jumpCnt += 1
            var furthest = 0
            (left...right).forEach {
                furthest = max(furthest, $0+nums[$0])
            }
            
            left = right+1
            right = furthest
        }
        
        return jumpCnt
    }
}
```