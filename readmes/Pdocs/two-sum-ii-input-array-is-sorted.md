# Two Sum II - Input Array Is Sorted
> **Easy**
>
> **2021-11-14**
>
> **[Leetcode: Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)**


## Sol

오름차순으로 정렬된 배열이 주어지고 배열 내 원소 두개를 합쳐서 target이 되는 원소들의 인덱스를 return하는 문제. 투 포인터를 사용하여 풀이해주었다.

## 답안
> Runtime: 56 ms, faster than 95.98% of Python3 online submissions for Two Sum II - Input Array Is Sorted.  
> Memory Usage: 14.6 MB, less than 63.45% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            result = numbers[l]+numbers[r]
            if result == target:
                return [l+1,r+1]
            elif result > target:
                r -= 1
            else:
                l += 1
            
```