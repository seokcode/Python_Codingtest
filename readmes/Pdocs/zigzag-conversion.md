# ZigZag Conversion
> **Medium**
>
> **2021-03-03**
>
> **[Leetcode: ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion)**


## Sol
```python
P   A   H   N # group[0]
A P L S I I G # group[1]
Y   I   R     # group[2]
```
idx가 0부터 시작하므로 idx+1이 numRows랑 같아지면 위의 그룹으로 move한다.  

## 답안
> Runtime: 48 ms, faster than 96.78% of Python3 online submissions for ZigZag Conversion.  
> Memory Usage: 14.2 MB, less than 87.39% of Python3 online submissions for ZigZag Conversion.
```python
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        
        groups = [""]*numRows
        idx, move = 0, 0
        
        for item in s:
            groups[idx] += item
            if idx == 0:
                move = 1
            elif idx+1 == numRows:
                move = -1
            idx += move
        
        return "".join(groups)
```