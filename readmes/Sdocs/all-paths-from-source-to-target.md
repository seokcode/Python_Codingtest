# All Paths From Source to Target
> **Medium**
>
> **2021-09-25**
>
> **[Leetcode: All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target)**


## Sol

Example 1:

![](https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg)

Input: graph = [[1,2],[3],[3],[]]  
Output: [[0,1,3],[0,2,3]]  
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.  

## 답안
> Runtime: 96 ms, faster than 31.65% of Swift online submissions for All Paths From Source to Target.  
> Memory Usage: 15.9 MB, less than 31.65% of Swift online submissions for All Paths From Source to Target.
```swift
class Solution {
    func allPathsSourceTarget(_ graph: [[Int]]) -> [[Int]] {
        var stack = [(0,[0])]
        var answer = [[Int]]()
        
        while stack.count > 0 {
            // info.0: now, info.1: path
            var info = stack.removeFirst()

            if info.0 == graph.count-1 {
                answer.append(info.1) 
            } 
            
            for nxt in graph[info.0] {
                stack.append((nxt, info.1 + [nxt]))
            }
        }        
        return answer
    }
}
```