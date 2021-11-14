# Move Zeroes
> **Easy**
>
> **2021-11-14**
>
> **[Leetcode: Move Zeroes](https://leetcode.com/problems/move-zeroes)**


## Sol

배열 내의 0을 찾아서 제거하고 배열 뒤에 붙이는 문제.  
filter를 사용하여 0을 없앤 배열을 만들고 원본 배열과의 길이 차이만큼 0을 붙여주었다.

## 답안
> Runtime: 152 ms, faster than 85.89% of Python3 online submissions for Move Zeroes.  
> Memory Usage: 15.4 MB, less than 30.59% of Python3 online submissions for Move Zeroes.
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        noneZeroArr = list(filter(lambda x: x != 0, nums))
        nums[:] = noneZeroArr + (len(nums) - len(noneZeroArr))*[0]
        """
        Do not return anything, modify nums in-place instead.
        """
        
```