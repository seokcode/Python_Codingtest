# Binary Search
> **Easy**
>
> **2021-11-07**
>
> **[Leetcode: 704. Binary Search](https://leetcode.com/problems/binary-search/)**


## Sol
> 이진탐색을 사용하려면 배열이 오름차순이어야한다.

주어진 nums 배열에 target이 있다면 그 인덱스를 return하는 문제. 없다면 -1를 return한다.
문제 이름처럼 이진탐색을 통해 풀이해주었다.

## 답안
> Runtime: 232 ms, faster than 85.87% of Python3 online submissions for Binary Search.  
> Memory Usage: 15.5 MB, less than 69.92% of Python3 online submissions for Binary Search.
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left ,right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right-left) //2
            
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1
```