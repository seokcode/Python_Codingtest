class Solution:
    def dfs(self, idx, visited, graph):
        if visited[idx] == "doing":
            return False
        if visited[idx] == "done":
            return True
        
        visited[idx] = "doing"
        
        for g in graph[idx]:
            if not self.dfs(g, visited, graph):
                return False   
            
        visited[idx] = "done"
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = ["notYet" for _ in range(numCourses)] 
        
        for x,y in prerequisites:
            graph[x].append(y)
        
        for i in range(numCourses):
            if not self.dfs(i, visited, graph):
                return False
            
        return True