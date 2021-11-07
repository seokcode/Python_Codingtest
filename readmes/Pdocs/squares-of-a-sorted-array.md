# Squares of a Sorted Array
> **Easy**
>
> **2021-11-07**
>
> **[Leetcode: 977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)**


## Sol
주어지는 nums 배열 내 숫자를 제곱하고 정렬된 배열로 만드는 문제

## 답안
> Runtime: 232 ms, faster than 67.44% of Python3 online submissions for Squares of a Sorted Array.
> Memory Usage: 15.8 MB, less than 91.16% of Python3 online submissions for Squares of a Sorted Array.
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x**2, nums)))
```