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