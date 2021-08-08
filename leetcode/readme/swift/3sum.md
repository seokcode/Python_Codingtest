# 3Sum
> **Medium**
>
> **2021-08-08**
>
> **[Leetcode: 15. 3Sum](https://leetcode.com/problems/3sum)**


## Sol

Constraints:
* 0 <= nums.length <= 3000
* -105 <= nums[i] <= 105


세 수의 합이 0인 조합을 구하기 위해 combination으로 모든 경우의 수를 구해주려하면 시간 초과가 나게 된다.
따라서 주어진 nums 배열을 정렬한 뒤 투 포인터를 이용하여 문제를 풀어주어야 한다.

##
```swift
class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        var res = Set<[Int]>()
        let n = nums.count
        let numArr = nums.sorted()
        
        for i in 0..<n {
            if i > 0 && numArr[i] == numArr[i-1] {
                continue
            }
            
            var j = i+1
            var r = n-1
            while j < r {
                let s = numArr[i] + numArr[j] + numArr[r]
                if s < 0 {
                    j += 1
                } else if  s > 0 {
                    r -= 1
                } else {
                    res.insert([numArr[i], numArr[j], numArr[r]])
                    j += 1
                    r -= 1
                }
            }
        }
        return Array(res)
    }
}
```