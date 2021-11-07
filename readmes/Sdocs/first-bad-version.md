# First Bad Version
> **Easy**
>
> **2021-11-07**
>
> **[Leetcode: 278. First Bad Version](https://leetcode.com/problems/first-bad-version/)**


## Sol
isBadVersion이라는 이미 정의된 API를 호출해서 1~n 의 버젼 중 몇번째 버젼이 가장 처음으로 Bad Version이 되었는지 return하는 문제.
> 만약 버젼 3이 첫 Bad Version이면 3 이상의 모든 버젼은 전부 Bad Version이다.

## 답안
> Runtime: 4 ms, faster than 69.03% of Swift online submissions for First Bad Version.
> Memory Usage: 13.6 MB, less than 94.36% of Swift online submissions for First Bad Version.
```swift
/**
 * The knows API is defined in the parent class VersionControl.
 *     func isBadVersion(_ version: Int) -> Bool{}
 */

class Solution : VersionControl {
    func firstBadVersion(_ n: Int) -> Int {
        var left = 1
        var right = n
        
        while left <= right {
            let mid = left + ((right-left)/2)
            if isBadVersion(mid) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        
        return left
    }
}
```