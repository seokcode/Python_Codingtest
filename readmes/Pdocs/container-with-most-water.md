# Container With Most Water
> **Medium**
>
> **2021-11-28**
>
> **[Leetcode: Container With Most Water](https://leetcode.com/problems/container-with-most-water/)**


## Sol
Input이  height = [1,8,6,2,5,4,8,3,7] 라고 주어지고 그걸 그림으로 아래처럼 나타낼 수 있을 때 막대를 두개 선택하여 이룰 수 있는 최대 넓이를 구하는 문제

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

## 답안
> Runtime: 652 ms, faster than 95.75% of Python3 online submissions for Container With Most Water.  
> Memory Usage: 27.4 MB, less than 83.50% of Python3 online submissions for Container With Most Water.
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_width = len(height)-1
        left, right = 0, len(height)-1
        area = 0
        
        for width in range(max_width, 0, -1):
            if height[left] < height[right]:
                area = max(area, width*height[left])
                left += 1
            else:
                area = max(area, width*height[right])
                right -= 1
        
        return area
```