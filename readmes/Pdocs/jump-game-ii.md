# Jump Game II
> **Medium**
>
> **2021-09-19**
>
> **[Leetcode: 45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)**


## Sol 
`완탐+DP`로 `memoization`을 활용하여 풀이하였다. 이는 O(N^2)의 시간복잡도가 소요된다.  

다른 방법으로는 `투 포인터`를 사용하는 방법이 있다.  
`left`는 갈 수 있는 최소 지점, `right`는 갈 수 있는 최대 지점이다. 만약 갈 수 있는 최대 지점이 lastIndex 이상이면 종료된다.

## DP 풀이
> Runtime: 9428 ms, faster than 12.76% of Python3 online submissions for Jump Game II.  
> Memory Usage: 15.4 MB, less than 12.63% of Python3 online submissions for Jump Game II.
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [0] + [float("inf")] * (len(nums)-1)
        
        for idx,i in enumerate(nums):
            for j in range(1,i+1):
                if idx+j < len(nums):
                    steps[idx+j] = min(steps[idx+j], steps[idx]+1)
       
        return steps[-1]
        
        # Time complexity: O(N^2)
        # Space complexity: O(1)
```

## Two Pointer 풀이
> 점프 횟수 별로 갈 수 있는 최대 거리를 계산해보는 방법.  
> Runtime: 120 ms, faster than 88.73% of Python3 online submissions for Jump Game II.  
> Memory Usage: 15.2 MB, less than 46.55% of Python3 online submissions for Jump Game II.

[2,3,1,1,4] 로 예를 들자.

1. [`2`,3,1,1,4] 
    * nJumps = 1
    * lp: 0, rp: 0, furthest: max(0+2) = 2
2. [2,`3,1`,1,4]
    * nJumps = 2
    * lp, rp = rp+1, furthest
    * lp: 1, rp: 2, furthest: max(1+3, 1+2) = `4` -> 목적지 도달, 끝!

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        # the initial range (after 0th jump) is [0,0]
        l = r = 0 # `l`: 갈 수 있는 최소 지점, `r`: 갈 수 있는 최대 지점
        nJumps = 0
        while r < len(nums) - 1:
            nJumps += 1
            furthest = max([i + nums[i] for i in range(l,r+1)])
            l,r = r+1, furthest

        return nJumps
        
        # Time complexity: O(N)
        # Space complexity: O(1)
```