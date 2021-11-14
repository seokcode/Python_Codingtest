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
> Runtime: 212 ms, faster than 85.74% of Python3 online submissions for Rotate Array.  
> Memory Usage: 25.5 MB, less than 84.43% of Python3 online submissions for Rotate Array.
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
        """
        Do not return anything, modify nums in-place instead.
        """
        
```