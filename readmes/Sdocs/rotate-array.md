# Rotate Array
> **Medium**
>
> **2021-11-14**
>
> **[Leetcode: Rotate Array](https://leetcode.com/problems/rotate-array)**


## Sol
k만큼 주어진 배열을 회전시켜주는 문제이다.

배열의 크기가 n이라면 n번 회전시켰을 때 다시 원점이므로 k를 n으로 나눈 나머지만큼만 회전을 시켜주었고 회전이 되는 만큼을 떼어서 앞에 붙여주는 식으로 풀이하였다.

## 답안
> Runtime: 252 ms, faster than 76.38% of Swift online submissions for Rotate Array.  
> Memory Usage: 21.4 MB, less than 47.10% of Swift online submissions for Rotate Array.
```swift
class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        var k = k % nums.count 
        let n = nums.count - 1
        reverse(&nums, 0, n)
        reverse(&nums, 0, k - 1)
        reverse(&nums, k, n)
    }
    
    func reverse(_ nums: inout [Int], _ s: Int, _ e: Int) {
        var s = s 
        var e = e 
        while s < e {
            nums.swapAt(s, e)
            s += 1
            e -= 1
        }
    }
}
```