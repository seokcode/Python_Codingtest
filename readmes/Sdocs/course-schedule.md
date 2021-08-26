# Course Schedule
> **Medium**
>
> **2021-08-26**
>
> **[Leetcode: Course Schedule](https://leetcode.com/problems/course-schedule)**


## Sol

[여행경로](https://programmers.co.kr/learn/courses/30/lessons/43164)와 비슷한 문제.

각 과목들은 수강하기위해서 선행되어야 하는 선행과목들이 존재한다. 주어진 과목들을 루프를 만들지 않고 다 들을 수 있는지 체크하면된다.
> 한가지 헷갈렸던 것은 과목 인덱스가 무조건 순서대로 주어지는지 좀 헷갈렸는데 맞는 것 같다.
> numCourses가 2면 0,1 과목이 주어지는 너낌


먼저 주어진 과목들을 토대로 인접리스트를 만들어주고 주어지는 코스의 갯수대로 for문을 돌며 각 과목을 듣기 위해 선행되어야하는 과목들이 문제가 없는지 체크해준다.


## 답안
```swift
class Solution {
    func dfs(_ idx: Int, _ graph: [[Int]], _ visited: inout [String]) -> Bool {
        if visited[idx] == "doing" {
            return false
        }
        if visited[idx] == "done" {
            return true
        }
        visited[idx] = "doing"
        for g in graph[idx] {
            if !dfs(g, graph, &visited) {
                return false
            }
        }
        visited[idx] = "done"        
        return true
    }
    
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
        var graph = Array(repeating: [Int](), count: numCourses)
        var visited = Array(repeating: "notYet", count: numCourses)
        
        for course in prerequisites {
            graph[course.first!].append(course.last!)   
        }
        
        for idx in 0..<numCourses {
            if !dfs(idx, graph, &visited) {
                return false
            }
        }        
        
        return true
    }
}
```