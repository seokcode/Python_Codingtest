# All Paths From Source to Target
> **Medium**
>
> **2021-03-03**
>
> **[Leetcode: All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target)**


## Sol

Example 1:

![](https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg)

Input: graph = [[1,2],[3],[3],[]]  
Output: [[0,1,3],[0,2,3]]  
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.  

## 답안
> Runtime: 100 ms, faster than 74.24% of Python3 online submissions for All Paths From Source to Target.  
> Memory Usage: 15.5 MB, less than 74.74% of Python3 online submissions for All Paths From Source to Target.
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        toGo = [(0,[0])]
        
        while toGo:
            cur, path = toGo.pop()
            
            if cur == len(graph)-1:
                answer.append(path)
            
            for i in graph[cur]:
                toGo.append((i,path+[i]))
            
        return answer
```