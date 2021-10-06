# ZigZag Conversion
> **Medium**
>
> **2021-10-06**
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
> Runtime: 56 ms, faster than 91.51% of Swift online submissions for ZigZag Conversion.  
> Memory Usage: 14.6 MB, less than 72.20% of Swift online submissions for ZigZag Conversion.
```swift
class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        if numRows == 1 { return s }
        
        var groups = Array(repeating: "", count: numRows)
        var idx = 0
        var step = 1

        for l in Array(s) {
            groups[idx] += "\(l)"
            
            if idx+step == numRows {
                step = -1
            } else if idx+step < 0 {
                step = 1
            }
            idx += step
        }
        
        return groups.reduce(""){ $0 + $1 }
    }
}
```