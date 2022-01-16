# Two Sum
> **Easy**
>
> **2022-01-16**
>
> **[Leetcode: Two Sum](https://leetcode.com/problems/two-sum)**


## Sol 

주어진 숫자 배열의 길이만큼만 순회한다.  
목표하는 숫자에서 현재 방문 숫자를 뺀 숫자가 배열에 존재하는지 확인하여 풀이한다. 

## 답안
> Runtime: 56 ms, faster than 91.78% of Python3 online submissions for Two Sum.  
> Memory Usage: 15.3 MB, less than 42.27% of Python3 online submissions for Two Sum.
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums): #1
            remaining = target - nums[i] #2
            
            if remaining in seen: #3
                return [i, seen[remaining]]  #4
            else:
                seen[value] = i  #5
```