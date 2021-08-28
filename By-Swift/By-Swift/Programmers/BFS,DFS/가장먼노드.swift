import Foundation

func solution(_ n:Int, _ edge:[[Int]]) -> Int {
    var graph = Array(repeating: [Int](), count: n+1)
    var visited = Array(repeating: 0, count: n+1)
    var queue = [(1,0)]
    
    for v in edge {
        graph[v.first!].append(v.last!)
        graph[v.last!].append(v.first!)
    }
    
    while !queue.isEmpty {
        let nodeInfo = queue.removeFirst()
        
        graph[nodeInfo.0].forEach {
            if visited[$0] == 0 {
                let value = nodeInfo.1 + 1
                visited[$0] = value
                queue.append(($0, value))
            }
        }
    }
    
    visited[1] = 0
    let max_v = visited.max()
    return visited.filter{$0 == max_v}.count
    return 0
}