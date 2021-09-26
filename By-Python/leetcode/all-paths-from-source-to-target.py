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