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