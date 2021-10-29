# Jump Game
> **Medium**
>
> **2021-10-29**
>
> **[Leetcode: 55. Jump Game](https://leetcode.com/problems/jump-game/)**


## Sol 

Jump Game II 문제처럼 Goal에 도달하는 최소 횟수가 아니라 Goal에 도달할 수 있는지 여부만을 확인하면 되는 문제이다. 투포인터로 풀어따

[2,3,1,1,4] 로 예를 들자.

1. [`2`,3,1,1,4]  
    * lp: 0, rp: 0, furthest: max(0+2) = 2
2. [2,`3,1`,1,4]
    * lp, rp = rp+1, furthest
    * lp: 1, rp: 2, furthest: max(1+3, 1+2) = `4` -> 목적지 도달, 끝!

[3,2,1,0,4] 로 예를 들자.

1. [`3`,2,1,0,4]
    * lp: 0, rp: 0, furthest: max(0+3) = 3
2. [3,`2,1,0`,4]
    * lp, rp = rp+1, furthest
    * lp: 1, rp: 3, furthest: max(1+2, 2+1, 3+0) = 3
2. [3,2,1,0,4]
    * lp, rp = rp+1, furthest
    * lp: 4, rp: 3 -> 전진 불가, 끝!

## 답안
> Runtime: 424 ms, faster than 99.25% of Swift online submissions for Jump Game.  
> Memory Usage: 14.2 MB, less than 72.75% of Swift online submissions for Jump Game.
```swift
class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        var pointer = (0,0)
        var furthest = 0
        let destination = nums.count-1
        
        while pointer.1 < destination {
            if pointer.0 > pointer.1 {
                return false
            }
            
            for i in pointer.0...pointer.1 {
                furthest = max(furthest, i+nums[i])
            }
            
            pointer = (pointer.1+1, furthest)
        }
        return true
    }
}   
```