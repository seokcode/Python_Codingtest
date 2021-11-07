# Search Insert Position
> **Easy**
>
> **2021-11-07**
>
> **[Leetcode: 35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)**


## Sol
> 이진탐색을 사용하려면 배열이 오름차순이어야한다.

주어지는 nums 배열에서 target의 위치를 return한다.  
만약 target이 nums에 없다면 들어갈 위치를 return한다.

## 답안
> Runtime: 52 ms, faster than 57.48% of Python3 online submissions for Search Insert Position.  
> Memory Usage: 14.9 MB, less than 81.94% of Python3 online submissions for Search Insert Position.
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + ((right-left) // 2)
            
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
```